from selenium import webdriver
from time import sleep

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Hello, tudo certo? ^^"
        self.grupos = ["Família", "Ninfa-sama"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # <span dir="auto" title="Ninfa-sama" class="_ccCW FqYAR i0jNr">Ninfa-sama</span>
        # <span dir="auto" title="Família" class="_ccCW FqYAR i0jNr">Família</span>
        # <div class="_13NKt copyable-text selectable-text" contenteditable="true" data-tab="6" dir="ltr" spellcheck="true"></div>
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        sleep(30)


        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title'{grupo}']")
            sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name("_13NKt copyable-text selectable-text")
            sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send'")
            sleep(3)
            botao_enviar.click()
            sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()
