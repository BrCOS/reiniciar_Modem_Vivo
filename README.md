
# Reniciar Modem Vivo

Código Python usando Selenium para reiniciar o modem da Vivo de forma simples e rápida.

Vale lembrar que o código deve ser utilizado com cuidado, pois os seus serviços de internet, tv e telefone irão ficar temporariamente indisponíveis após a reinicialização do seu modem.

**Aviso Importante: Uso Responsável do Código**

*Este código é fornecido apenas para fins educacionais e de aprendizado. Não me responsabilizo pelo uso indevido ou inadequado deste código para qualquer finalidade não autorizada.*

*É fundamental entender que o acesso e a manipulação de sistemas, redes ou dispositivos sem a devida autorização podem ser ilegais e violar as políticas de privacidade e segurança. Utilizar esse código de forma inadequada ou para fins maliciosos pode acarretar em consequências legais graves.*

*Portanto, recomendo veementemente que o código seja utilizado de acordo com as leis aplicáveis e com o devido consentimento e permissão dos proprietários do sistema ou dispositivo em questão.*

*O conhecimento e a compreensão dos princípios subjacentes ao código são valiosos para o desenvolvimento de habilidades e competências na área de programação e segurança da informação. Utilize esse conhecimento de maneira ética e responsável, contribuindo para um ambiente digital mais seguro e confiável.*

*Lembre-se de sempre respeitar a privacidade e os direitos de terceiros ao utilizar qualquer código ou técnica aprendida através desse material.*

*Se tiver dúvidas sobre a aplicação ética deste código, busque orientação de profissionais ou especialistas na área antes de prosseguir com qualquer ação.*

## Como encontrar a senha do Modem?

Na frente do modem: Geralmente, em uma etiqueta, você pode localizar a senha após a frase "No app, digite a senha". Ela estará logo após essa indicação.

Na parte debaixo do modem: Verifique a etiqueta localizada na parte inferior do modem. Nessa etiqueta, é comum encontrar a seção "Dados de Acesso ao Roteador", onde estarão listados tanto o usuário quanto a senha necessária para a configuração.

Lembre-se de que a senha para configurar o modem é diferente da senha do seu Wi-Fi. Mantenha essas informações em um local seguro, pois elas são essenciais para realizar alterações na configuração do seu modem e garantir o acesso à rede de forma adequada.
## Como usar?

Depois de encontrar a senha de configuração do modem, siga o passo abaixo para configurá-la no código:

```python
senha.send_keys('SUA SENHA AQUI')
```

Substitua 'SUA SENHA AQUI' pela sua senha de configuração do modem. Certifique-se de manter as aspas ao redor da senha, para que o código funcione corretamente.
## Requerimentos
Para utilizar o script com eficiência, é necessário atender dois requisitos básicos:

**Navegador Google Chrome instalado**: O script foi desenvolvido para funcionar com o navegador Google Chrome. Certifique-se de ter o Chrome instalado no seu sistema antes de executar o código.

**Ambiente virtual e instalação de dependências**: É altamente recomendado criar um ambiente virtual para isolar as dependências do projeto. Isso garante que as bibliotecas e pacotes necessários para o script não interfiram em outras aplicações Python no seu sistema.

Após a criação e ativação do ambiente virtual, instale as dependências do projeto através do código:

```python
pip install -r requirements.txt
```

Lembre-se de criar e ativar seu ambiente virtual antes de instalar as dependências do projeto!
