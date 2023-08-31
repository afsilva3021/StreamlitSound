import streamlit as st
import PIL as Image




def home():
    
    c1,c2,c3 = st.columns(3, gap="large")
    
    with c2:
        st.title("Music Cloud")

        st.image("./img/soundcloud.jpg")
      
    st.write("""
                oundCloud é uma plataforma online de publicação de áudio utilizada por profissionais de música sediada em Berlim, Alemanha, fundada por Alexander Ljung e Eric Wahlforss em Agosto de 2007. Nela os músicos podem colaborar, compartilhar, promover e distribuir suas composições.

Originalmente, o objetivo do site era permitir que profissionais da música trocassem ideias sobre as composições nas quais estão trabalhando, permitindo uma fácil colaboração e comunicação antes de um lançamento público. Hoje, o site também é utilizado por ouvintes e usuários da web em geral.

O site permite mostrar os arquivos de áudio enviados em widgets que simulam um diagrama de espectro abaixo do qual os usuários podem postar seus comentários sobre a música. Estes widgets podem ser embutidos em blogs e redes sociais.

Entre os usuário ilustres do site estão o produtor americano Beck Hansen, o duo de música eletrônica The Knife e a banda de rock Them Crooked Vultures.

Atualmente, as músicas postadas no site são também indexadas pelo site agregador de áudio Hype Machine.

Em 3 de Julho de 2014 o site TorrentFreak informou que o SoundCloud ofereceu poderes de remoção ilimitados a certos detentores de direitos autorais. Em resposta a uma reclamação de um DJ inglês a empresa admitiu que a Universal Music pode deletar qualquer faixa do SoundCloud sem aviso prévio.



""")