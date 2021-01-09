# importar pacotes
import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageEnhance

def main():
    # main
    st.title('Masterclass Visão Computacional')
    st.text('Sigmoidal')
    st.sidebar.title('Barra Lateral')

    # menu com opções de páginas
    opcoes_menu = ['Filtros', 'Sobre']
    escolha = st.sidebar.selectbox('Escolha uma opção', opcoes_menu)

    if escolha == 'Filtros':

        # carregar variáveis iniciais
        output_width = 300
        our_image = Image.open('empty.jpg')
        
        # carregar e exibir imagem
        image_file = st.file_uploader('Carregue uma foto e aplique um filtro no menu lateral', type=['jpg', 'jpeg', 'png'])

        if image_file is not None:
            our_image = Image.open(image_file)
            st.sidebar.text('Imagem Original')
            st.sidebar.image(our_image, width=150)
            filtros = st.sidebar.radio('Filtros', ['Original', 'Grayscale', 'Desenho', 'Sépia', 'Blur', 'Canny', 'Contraste'])

            # Filtros que podem ser aplicados
            if filtros == 'Grayscale':
                converted_image = np.array(our_image.convert('RGB'))
                gray_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2GRAY)
                st.image(gray_image, width=output_width)

            elif filtros == 'Desenho':
                converted_image = np.array(our_image.convert('RGB'))
                gray_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2GRAY)
                inv_gray_image = 255 - gray_image
                blur_image = cv2.GaussianBlur(inv_gray_image, (21, 21), 0, 0)
                sketch_image = cv2.divide(gray_image, 255 - blur_image, scale=256)
                st.image(sketch_image, width=output_width)

            elif filtros == 'Sépia':
                converted_image = np.array(our_image.convert('RGB'))
                converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
                kernel = np.array([[0.272, 0.534, 0.131],
                        [0.349, 0.686, 0.168],
                        [0.393, 0.769, 0.189]])
                sepia_image = cv2.filter2D(converted_image, -1, kernel)
                st.image(sepia_image, channels ='BGR',width=output_width)

            elif filtros == 'Blur':
                b_amount = st.sidebar.slider('Kernel (n x n)', 3, 81, 9, step=2)
                converted_image = np.array(our_image.convert('RGB'))
                converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
                blur_image = cv2.GaussianBlur(converted_image, (b_amount, b_amount), 0, 0)
                st.image(blur_image, channels='BGR', width=output_width)

            elif filtros == 'Canny':
                converted_image = np.array(our_image.convert('RGB'))
                converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
                blur_image = cv2.GaussianBlur(converted_image, (11, 11), 0, 0)
                canny = cv2.Canny(blur_image, 100, 150)
                st.image(canny, width=output_width)
            
            elif filtros == 'Contraste':
                c_amount = st.sidebar.slider('Contraste', 0.0, 2.0, 1.0)
                enhancer = ImageEnhance.Contrast(our_image)
                contraste_image = enhancer.enhance(c_amount)
                st.image(contraste_image, width=output_width)

            elif filtros == 'Original' and image_file is not None:
                st.image(our_image, width=output_width)

        else:
            st.image(our_image, width=output_width)

    elif escolha == 'Sobre':
        st.subheader('Este é um projeto da Masterclass de Visão Computcional, do Sigmoidal')
        st.markdown('Para saber mais informações acesse [Sigmoidal.ai](https://sigmoidal.ai)')

# Iniciar a aplicação
if __name__ == '__main__':
    main()