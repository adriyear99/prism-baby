import pygame,pygame.mixer
import os
import sys
import random

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

#Váriaveis do Jogo
sexo_Escolhido = "indefinido"
comida_selecionada = "vazio"
bebida_selecionada = "vazio"
comida_anim = 0
bebida_anim = 0
box_necessidades_sede_anim = 0
box_necessidades_comida_anim = 0
lavar = 3
x = 0
anim_maos = 0
flag_menu_config_aberto = False
cookie = True
burger = True
mamadeira = True
milkshake = True
torneira = False
tampa = False
secar = False
bolha = False
rasgar = False
limpar = False
descarga = False
switch = False
comida_full = False
bebida_full = False

#Atributos de Cenas
#Menu Principal
Painel_                     =               (25,100,300,400)
Painel_Jogar                =               (30,225,290,200)
Painel_Creditos             =               (40,380,120,120)
creditos2                   =               (90,320,120,120)
Painel_Sair                 =               (180,380,125,120)
sair2                       =               (230,320,125,120)
Btn_Voltar                  =               (10,10,70,70)
Btn_RemoverSom              =               (650,10,50,50)
Btn_AtivarSom               =               (710,10,50,50)
Vitoria                     =               (30,180,400,200)
nome                        =               (30,100,550,200)
nome2                       =               (20,300,550,200)

#Tela de Seleção
btn_SelecaoMasculino        =               (150,170,150,200)
btn_SelecaoFeminino         =               (500,170,150,200)
ico_SexoIndefinido          =               (350,220,100,100)
ico_SexoMasculino           =               (350,220,100,100)
ico_SexoFeminino            =               (350,220,100,100)

#Cozinha
prato                       =               (200,400,400,200)
bebida                      =               (630,300,90,250)
porta_masculina             =               (540,95,100,250)
porta_feminina              =               (670,95,100,250)
btnMenu_Config              =               (710,10,50,50)
box_menu_config_aberto      =               (200,50,400,400)
box_menu_fechar             =               (520,70,50,50)
box_menu_ComSom             =               (370,150,50,50)
box_menu_SemSom             =               (440,150,50,50)
btn_menu_VoltarTelaInicial  =               (350,345,100,100)
box_status                  =               (0,0,500,100)

cookie_icon                 =               (20,15,70,70)
burger_icon                 =               (120,15,70,70)
mamadeira_icon              =               (235,15,50,70)
milkshake_icon              =               (345,15,60,70)
comida_position             =               (220,370,350,200)
bebida_position             =               (630,300,90,250)
setaH                       =               (440,140,100,100)
setaM                       =               (590,140,100,100)
box_necessidades            =               (0,350,120,250)
box_necessidades_comida     =               (20,370,90,90)
box_necessidades_sede       =               (10,470,100,100)

#Banheiro
pia                         =               (15,280,200,200)
privada                     =               (500,350,200,200)
porta_banheiro              =               (280,185,160,300)
btnMenu_Config              =               (710,10,50,50)
box_menu_config_aberto      =               (200,50,400,400)
box_menu_fechar             =               (520,70,50,50)
box_menu_ComSom             =               (370,150,50,50)
box_menu_SemSom             =               (440,150,50,50)
btn_menu_VoltarTelaInicial  =               (350,345,100,100)
torneira_desligada          =               (150,280,500,400)
torneira_ligada             =               (150,280,500,400)
espelho                     =               (200,100,400,250)
toalha                      =               (10,370,200,200)
saboneteira                 =               (650,350,60,60)
sabao                       =               (655,355,50,50)
sabao2                      =               (655,355,50,50)
vaso_fechado                =               (100,160,500,500)
vaso_aberto                 =               (100,170,500,500)
papel                       =               (570,370,150,150)
papel2                      =               (570,370,150,150)
xixi_icon                   =               (200,50,100,100)
coco_icon                   =               (350,50,100,100)
setaPrivada                 =               (430,400,100,100)
setaTorneira                =               (180,280,100,100)
setaPapel                   =               (500,400,100,100)
alavanca                    =               (70,250,200,100)

def resetar():
    global box_necessidades_sede_anim
    global box_necessidades_comida_anim
    global comida_anim
    global comida_selecionada
    global comida_full
    global x
    global anim_maos
    global cookie
    global burger
    global bebida_anim
    global bebida_selecionada
    global bebida_full
    global tampa
    global torneira
    global mamadeira
    global milkshake
    global bolha
    global lavar
    global rasgar
    global limpar
    global secar
    global reflexo
    global descarga
    global switch

    x = 0
    anim_maos = 0
    comida_anim = 0
    box_necessidades_comida_anim = 0
    bebida_anim = 0
    box_necessidades_sede_anim = 0
    comida_selecionada = "vazio"
    bebida_selecionada = "vazio"
    lavar = 3
    comida_full = False
    bebida_full = False
    cookie = True
    burger = True
    mamadeira = True
    milkshake = True
    bolha = False
    tampa = False
    secar = False
    rasgar = False
    limpar = False
    torneira = False
    descarga = False
    switch = False

#Importando Som
som_background0 = pygame.mixer.Sound('tracks/backgroundzero.wav')
som_background2 = pygame.mixer.Sound('tracks/backgrounddois.wav')
som_clique = pygame.mixer.Sound('tracks/som_clique.wav')
som_torneira = pygame.mixer.Sound('tracks/som_torneira.wav')
som_descarga = pygame.mixer.Sound('tracks/som_descarga.wav')
som_xixi = pygame.mixer.Sound('tracks/som_xixi.wav')
som_coco = pygame.mixer.Sound('tracks/som_coco.wav')
som_papel = pygame.mixer.Sound('tracks/som_papel.wav')
som_toalha = pygame.mixer.Sound('tracks/som_toalha.wav')
som_sabao = pygame.mixer.Sound('tracks/som_sabao.wav')
som_mordida = pygame.mixer.Sound('tracks/som_mordida.wav')
som_bebida = pygame.mixer.Sound('tracks/som_bebida.wav')
som_erro = pygame.mixer.Sound('tracks/som_erro.wav')

def Exibir_Imagem(dados,nome):
    pos_x,pos_y,largura,altura = dados
    image = pygame.image.load(os.path.join("images",nome))
    image = pygame.transform.scale(image,(largura,altura))
    screen.blit(image,(pos_x,pos_y))

def Exibir_background(nome): #800x600
    image = pygame.image.load(os.path.join("images",nome))
    screen.blit(image,(0,0))

anim_passaro = 0
passaro_x = random.randint(-10,600)
passaro_y = random.randint(0,200)
passaro_sprite = []
for i in range(7):
    passaro_sprite.append(pygame.image.load(os.path.join("images//passaros",'frame_' + str(i) + '_delay-0.08s.png')))
    
def anima_passaro():
    global anim_passaro
    global passaro_x
    global passaro_y

    passaro_y -= 1
    if(passaro_y >= 600):
        passaro_y = random.randint(0,200)
        anim_passaro = 0
    anim_passaro += 1
    if (anim_passaro >= 7):
        anim_passaro = 0
    passaro_x += 5
    if(passaro_x >= 800):
        passaro_x = random.randint(-10,0)
        passaro_y = random.randint(0, 200)

    index = pygame.transform.scale(passaro_sprite[anim_passaro],(200,200))
    screen.blit(index,(passaro_x, passaro_y))


def Exibir(cena):
    global anim_passaro
    global flag_menu_config_aberto
    #Atualizando Cenário
    if(cena == 0):
        Exibir_background('background_menu800x600_novo.jpg')
        anima_passaro()

        Exibir_Imagem(Painel_,'painel_menu.png')
        Exibir_Imagem(Painel_Jogar,'btn_menu_jogar.png')
        Exibir_Imagem(Painel_Creditos,'btn_menu_creditos.png')
        Exibir_Imagem(Painel_Sair,'btn_menu_sair.png')

        if(flag_cena_song == True):
            Exibir_Imagem(Btn_RemoverSom,'icone_semSom.png')
        else:
            Exibir_Imagem(Btn_AtivarSom,'icone_comSom.png')       
        screen.blit(pygame.font.SysFont("Arial bold",22).render("Desenvolvido por Monzeu Corporation - Versão Alpha 1.0",True,(255,255,255)),[10,5])
        
    elif(cena == 1):
        Exibir_background('background_selecao_sexo800x600.jpeg')
        Exibir_Imagem(Btn_Voltar,'btn_voltar.png')
        Exibir_Imagem(btn_SelecaoMasculino,'escolha_masculino.jpeg')
        Exibir_Imagem(btn_SelecaoFeminino,'escolha_feminino.jpeg')
        
        if(sexo_Escolhido == "indefinido"):
            Exibir_Imagem(ico_SexoIndefinido,'simbolo_indefinido.png')
        elif(sexo_Escolhido == "masculino"):
            Exibir_Imagem(ico_SexoMasculino,'simbolo_masculino.png')
        elif(sexo_Escolhido == "feminino"):
            Exibir_Imagem(ico_SexoFeminino,'simbolo_feminino.png')

    elif(cena == 2):
        Exibir_background('background_cozinha800x600.jpg')
        Exibir_Imagem(porta_masculina,'banheiro_masculino.png')
        Exibir_Imagem(porta_feminina,'banheiro_feminino.png')
        Exibir_Imagem(prato,'prato.png')
        Exibir_Imagem(btnMenu_Config,'btn_Menu_Opcoes.png')
        Exibir_Imagem(box_status,'barra_status.png')
        Exibir_Imagem(cookie_icon,'comida_cookie_icon.png')
        Exibir_Imagem(burger_icon,'comida_burger_icon.png')
        Exibir_Imagem(mamadeira_icon,'bebida_mamadeira_icon.png')
        Exibir_Imagem(milkshake_icon,'bebida_milkshake_icon.png')

        #necessidades
        Exibir_Imagem(box_necessidades,'barra_necessidades.png')
        Exibir_Imagem(box_necessidades_sede,'anim_status/pipi_' + str(box_necessidades_sede_anim) + '.png')
        Exibir_Imagem(box_necessidades_comida,'anim_status/fome_' + str(box_necessidades_comida_anim) + '.png')
        

        #Exibindo Comida selecionada no prato
        if(comida_selecionada != "vazio"):
            Exibir_Imagem(comida_position,'anim_comida/comida_' + comida_selecionada + '_' + str(comida_anim) + '.png')

        if(bebida_selecionada != "vazio"):
            Exibir_Imagem(bebida_position,'anim_bebida/bebida_' + bebida_selecionada + '_' + str(bebida_anim) + '.png')

        if(comida_full == True or bebida_full == True):
            if sexo_Escolhido == "masculino":
                Exibir_Imagem(setaH,'seta.png')
            else:
                Exibir_Imagem(setaM,'seta.png')

        if(cookie == False):
            Exibir_Imagem(cookie_icon,'x.png')
            
        if(burger == False):
            Exibir_Imagem(burger_icon,'x.png')
            
        if(mamadeira == False):
            Exibir_Imagem(mamadeira_icon,'x.png')
            
        if(milkshake == False):
            Exibir_Imagem(milkshake_icon,'x.png')            
            
    
        if(flag_menu_config_aberto == True):
            Exibir_Imagem(box_menu_config_aberto,'box_menu_config_aberto.png')
            Exibir_Imagem(box_menu_fechar,'btn_Fechar.png')
            Exibir_Imagem(btn_menu_VoltarTelaInicial,'btn_menu_voltarAoMenu.png')
            
            screen.blit(pygame.font.SysFont("Arial bold",46).render("SOM : ",True,(0,0,0)),[240,165])
            if(flag_cena_song == True):
                Exibir_Imagem(box_menu_SemSom,'icone_semSom.png')  
            else:
                Exibir_Imagem(box_menu_ComSom,'icone_comSom.png')  
            
        
    elif(cena == 3):
        Exibir_background('background_banheiro800x600.jpg')   
        Exibir_Imagem(porta_banheiro,'porta_banheiro.png')
        Exibir_Imagem(btnMenu_Config,'btn_Menu_Opcoes.png')
        Exibir_Imagem(pia,'pia.png')
        Exibir_Imagem(privada,'privada.png')

        if(bebida_full == True or comida_full == True):
            Exibir_Imagem(setaPrivada,'seta.png')

        if(lavar < 3):
            Exibir_Imagem(setaTorneira,'seta2.png')

        if(flag_menu_config_aberto == True):
            Exibir_Imagem(box_menu_config_aberto,'box_menu_config_aberto.png')
            Exibir_Imagem(box_menu_fechar,'btn_Fechar.png')
            Exibir_Imagem(btn_menu_VoltarTelaInicial,'btn_menu_sair.png')
            
            screen.blit(pygame.font.SysFont("Arial bold",46).render("SOM : ",True,(0,0,0)),[230,165])
            if(flag_cena_song == True):
                Exibir_Imagem(box_menu_SemSom,'icone_semSom.png')  
            else:
                Exibir_Imagem(box_menu_ComSom,'icone_comSom.png')

    elif(cena == 4):
        Exibir_background('background_banheiro2.jpg')
        Exibir_Imagem(btnMenu_Config,'btn_Menu_Opcoes.png')
        Exibir_Imagem(Btn_Voltar,'btn_voltar.png')
        Exibir_Imagem(espelho,'espelho.png')
        Exibir_Imagem(saboneteira,'saboneteira.png')

        
        
        if(secar == True):
            Exibir_Imagem(toalha,'toalha2.png')
        else:
            Exibir_Imagem(toalha,'toalha.png')
            
        if(torneira == True):
            Exibir_Imagem(torneira_ligada,'pia_ligada.png')
        else:
            Exibir_Imagem(torneira_desligada,'pia.png')

        if(bolha == True):
            Exibir_Imagem(sabao2,'sabao2.png')
        else:
            Exibir_Imagem(sabao,'sabao.png')

        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        Exibir_Imagem((Mouse_x-150,Mouse_y-150,300,300),'anim_maos/maos_' + str(anim_maos) + '.png')

        if(flag_menu_config_aberto == True):
            Exibir_Imagem(box_menu_config_aberto,'box_menu_config_aberto.png')
            Exibir_Imagem(box_menu_fechar,'btn_Fechar.png')
            Exibir_Imagem(btn_menu_VoltarTelaInicial,'btn_menu_sair.png')
            
            screen.blit(pygame.font.SysFont("Arial bold",46).render("SOM : ",True,(0,0,0)),[230,165])
            if(flag_cena_song == True):
                Exibir_Imagem(box_menu_SemSom,'icone_semSom.png')  
            else:
                Exibir_Imagem(box_menu_ComSom,'icone_comSom.png')

    elif(cena == 5):
        Exibir_background('background_banheiro2.jpg')
        Exibir_Imagem(btnMenu_Config,'btn_Menu_Opcoes.png')
        Exibir_Imagem(Btn_Voltar,'btn_voltar.png')

        
        if(tampa == True):
            Exibir_Imagem(vaso_aberto,'privada.png')
            if(switch == False):
                Exibir_Imagem(alavanca,'alavanca.png')
                if(descarga == True):
                    Exibir_Imagem(alavanca,'circulo.png')
            else:
                Exibir_Imagem(alavanca,'alavanca2.png')
        else:
            Exibir_Imagem(vaso_fechado,'privada_fechada.png')


        if(rasgar == True):
            Exibir_Imagem(papel2,'papel2.png')
        else:
            Exibir_Imagem(papel,'papel.png')

        if(limpar == True):
            Exibir_Imagem(setaPapel,'seta.png')

        if(bebida_full == True):
            Exibir_Imagem(xixi_icon,'xixi_ON.png')
        else:
            Exibir_Imagem(xixi_icon,'xixi_OFF.png')

        if(comida_full == True):
            Exibir_Imagem(coco_icon,'coco_ON.png')
        else:
            Exibir_Imagem(coco_icon,'coco_OFF.png')

        if(flag_menu_config_aberto == True):
            Exibir_Imagem(box_menu_config_aberto,'box_menu_config_aberto.png')
            Exibir_Imagem(box_menu_fechar,'btn_Fechar.png')
            Exibir_Imagem(btn_menu_VoltarTelaInicial,'btn_menu_sair.png')
            
            screen.blit(pygame.font.SysFont("Arial bold",46).render("SOM : ",True,(0,0,0)),[230,165])
            if(flag_cena_song == True):
                Exibir_Imagem(box_menu_SemSom,'icone_semSom.png')  
            else:
                Exibir_Imagem(box_menu_ComSom,'icone_comSom.png')

    elif(cena == 6):
        Exibir_background('background_menu800x600_novo.jpg')
        Exibir_Imagem(Vitoria,'vitoria.png')
        Exibir_Imagem(creditos2,'btn_menu_creditos.png')
        Exibir_Imagem(sair2,'btn_menu_sair.png')
        anima_passaro()

    elif(cena == 7):
        Exibir_background('background_menu800x600_novo.jpg')
        Exibir_Imagem(Btn_Voltar,'btn_voltar.png')
        Exibir_Imagem(nome,'creditos.png')
        Exibir_Imagem(nome2,'creditos2.png')
        anima_passaro()

def log(texto):
    print(f"REGISTRO: {texto}")

def Acoes(cena):
    global flag_cena_song
    global som_background0
    global sexo_Escolhido
    global prato
    global x
    global cookie
    global burger
    global mamadeira
    global milkshake
    global torneira
    global secar
    global reflexo
    global bolha
    global tampa
    global descarga
    global switch
    global rasgar
    global limpar
    global lavar
    global xixi
    global coco
    global flag_menu_config_aberto
    global comida_selecionada
    global comida_anim
    global comida_full
    global bebida_selecionada
    global bebida_anim
    global bebida_full
    global box_necessidades_sede_anim
    global box_necessidades_comida_anim
    global anim_maos
    
    for event in pygame.event.get():

       if event.type == pygame.MOUSEMOTION:
           if(cena == 4):
                #Definindo Colisao 
                btn_agua = pygame.Rect(torneira_ligada)
                
                if(torneira == True):
                  if btn_agua.collidepoint(event.pos):
                    if(anim_maos > 0):
                        anim_maos -= 1
                        log("Limpando Mãos")
                        
       elif event.type == pygame.MOUSEBUTTONDOWN:
           ##Cena 0
            if(cena == 0):
                #Definindo Colisao
                btnJogarColisao = pygame.Rect(Painel_Jogar)
                btnCreditosColisao = pygame.Rect(Painel_Creditos)
                btnSairColisao = pygame.Rect(Painel_Sair)
                btnJogarColisao = pygame.Rect(Painel_Jogar)
                btnPausarSomColisao = pygame.Rect(Btn_RemoverSom)
                btnContinuarSomColisao = pygame.Rect(Btn_AtivarSom)
                
                #Definindo Ações
                if btnJogarColisao.collidepoint(event.pos):
                    log("Clicando em Jogar")
                    log("Indo para tela de seleção")
                    sexo_Escolhido = "indefinido"
                    som_clique.play()
                    return cena+1
                
                elif btnCreditosColisao.collidepoint(event.pos):
                    log("Créditos")
                    som_clique.play()
                    return cena+7

                elif btnSairColisao.collidepoint(event.pos):
                    log("Sair")
                    som_clique.play()
                    pygame.quit()
                    sys.exit()
                    
                elif btnPausarSomColisao.collidepoint(event.pos):
                    flag_cena_song = False
                elif btnContinuarSomColisao.collidepoint(event.pos):
                    flag_cena_song = True
                    
            elif(cena == 1):
                #Definindo Colisao
                btnVoltarColisao = pygame.Rect(Btn_Voltar)
                btnEscolher_MeninoColisao = pygame.Rect(btn_SelecaoMasculino)
                btnEscolher_FemininoColisao = pygame.Rect(btn_SelecaoFeminino)

                if btnVoltarColisao.collidepoint(event.pos):
                    som_clique.play()
                    log(f"Cliando em Voltar")
                    return cena-1

                elif btnEscolher_MeninoColisao.collidepoint(event.pos):
                    sexo_Escolhido = "masculino"
                    som_clique.play()
                    log(f"Selecionando Sexo {sexo_Escolhido}")
                    log(f"Indo para cozinha")
                    som_background0.stop()
                    som_background2.play(loops = -1)
                    return cena+1

                elif btnEscolher_FemininoColisao.collidepoint(event.pos):
                    sexo_Escolhido = "feminino"
                    som_clique.play()
                    log(f"Selecionando Sexo {sexo_Escolhido}")
                    log(f"Indo para cozinha")
                    som_background0.stop()
                    som_background2.play(loops = -1)
                    return cena+1
                
            elif(cena == 2):
                #Definindo Colisao
                pratoColisao                       = pygame.Rect(prato)
                bebidaColisao                      = pygame.Rect(bebida)
                portaMasculinaColisao              = pygame.Rect(porta_masculina)
                portaFemininaColisao               = pygame.Rect(porta_feminina)
                btn_Config_AbrirColisao            = pygame.Rect(btnMenu_Config)
                btn_Config_FecharColisao           = pygame.Rect(box_menu_fechar)
                btn_Config_menu_SemSomColisao      = pygame.Rect(box_menu_SemSom)
                btn_Config_menu_ComSomColisao      = pygame.Rect(box_menu_ComSom)
                btn_menu_VoltarTelaInicialColisao  = pygame.Rect(btn_menu_VoltarTelaInicial)
                btn_colisao_cookie_icon            = pygame.Rect(cookie_icon)
                btn_colisao_burger_icon            = pygame.Rect(burger_icon)
                btn_colisao_mamadeira_icon         = pygame.Rect(mamadeira_icon)
                btn_colisao_milkshake_icon         = pygame.Rect(milkshake_icon)

                if(flag_menu_config_aberto == False):
                    if pratoColisao.collidepoint(event.pos):
                        som_clique.play()
                        if(comida_selecionada == "vazio"):
                            som_erro.play()
                            log("Clicando no prato vazio")
                        else:
                            if(box_necessidades_comida_anim < 5):
                                box_necessidades_comida_anim += 1
                                comida_anim += 1
                                som_mordida.play()
                                log(f"Comendo {comida_selecionada}")
                            else:
                                log(f"Bebê terminou de comer o {comida_selecionada}")
                                comida_anim = 0
                                som_mordida.stop()
                                comida_full = True
                                if(comida_selecionada == "cookie"):
                                    cookie = False
                                elif(comida_selecionada == "burger"):
                                    burger = False
                                comida_selecionada = "vazio"
                            
                    elif bebidaColisao.collidepoint(event.pos):              
                        som_clique.play()
                        if(bebida_selecionada == "vazio"):
                            som_erro.play()
                            log("Clicando na garrafa vazia")
                        else:
                            if(box_necessidades_sede_anim < 5):
                                box_necessidades_sede_anim += 1
                                bebida_anim += 1
                                som_bebida.play()
                                log(f"Bebendo {bebida_selecionada}")
                            else:
                                log(f"Bebê terminou de beber {bebida_selecionada}")
                                bebida_anim = 0
                                som_bebida.stop()
                                bebida_full = True                         
                                if(bebida_selecionada == "mamadeira"):
                                    mamadeira = False
                                elif(bebida_selecionada == "milkshake"):
                                    milkshake = False
                                bebida_selecionada = "vazio"                              

                    elif btn_colisao_cookie_icon.collidepoint(event.pos):
                        if comida_selecionada == "burger":
                            som_erro.play()
                            log("Você tem que terminar de comer primeiro")
                        elif cookie == True and box_necessidades_comida_anim < 5:
                            comida_anim = 0
                            comida_selecionada = "cookie"
                            log("Selecionando Cookie")
                        elif cookie == False:
                            som_erro.play()
                            log("Cookie já foi consumido")
                        else:
                            som_erro.play()
                            log("Bebê está cheio e precisa fazer cocô")
                            
                    elif btn_colisao_burger_icon.collidepoint(event.pos):
                        if comida_selecionada == "cookie":
                            som_erro.play()
                            log("Você tem que terminar de comer primeiro")
                        elif burger == True and box_necessidades_comida_anim < 5:
                            comida_anim = 0
                            comida_selecionada = "burger"
                            log("Selecionando Hambúrguer")
                        elif burger == False:
                            som_erro.play()
                            log("Hambúrguer já foi consumido")
                        else:
                            som_erro.play()
                            log("Bebê está cheio e precisa fazer cocô")
                            
                    elif btn_colisao_mamadeira_icon.collidepoint(event.pos):
                        if bebida_selecionada == "milkshake":
                            som_erro.play()
                            log("Você tem que terminar de beber primeiro")
                        elif mamadeira == True and box_necessidades_sede_anim < 5:
                            bebida_anim = 0
                            bebida_selecionada = "mamadeira"
                            log("Selecionando Mamadeira")
                        elif mamadeira == False:
                            som_erro.play()
                            log("Mamadeira já foi consumida")
                        else:
                            som_erro.play()
                            log("Bebê está cheio e precisa fazer xixi")
                                
                    elif btn_colisao_milkshake_icon.collidepoint(event.pos):
                        if bebida_selecionada == "mamadeira":
                            som_erro.play()
                            log("Você tem que terminar de beber primeiro")
                        elif milkshake == True and box_necessidades_sede_anim < 5:
                            bebida_anim = 0
                            bebida_selecionada = "milkshake"
                            log("Selecionando Milk-Shake")
                        elif milkshake == False:
                            som_erro.play()
                            log("Milk-Shake já foi consumido")
                        else:
                            som_erro.play()
                            log("Bebê está cheio e precisa fazer xixi")

                    elif portaMasculinaColisao.collidepoint(event.pos):
                        if(sexo_Escolhido == "masculino"):
                            log("Entrou no banheiro masculino")
                            return cena+1
                        else:
                            som_erro.play()
                            log(f"Proibido pois sexo {sexo_Escolhido} não pode entrar.")
                            
                    elif portaFemininaColisao.collidepoint(event.pos):
                        if(sexo_Escolhido == "feminino"):
                            log("Entrou no banheiro feminino")
                            return cena+1
                        else:
                            som_erro.play()
                            log(f"Proibido pois sexo {sexo_Escolhido} não pode entrar.")
                        
                else:
                    if btn_Config_menu_SemSomColisao.collidepoint(event.pos):
                        flag_cena_song = False
                        log("Desligando Som")
                    elif btn_Config_menu_ComSomColisao.collidepoint(event.pos):
                        flag_cena_song = True
                        log("Ligando Som")
                    elif btn_menu_VoltarTelaInicialColisao.collidepoint(event.pos):
                        flag_menu_config_aberto = False
                        som_background0.play(loops = -1)
                        som_background2.stop()
                        som_mordida.stop()
                        som_bebida.stop()
                        log("Voltando para Tela Inicial")
                        resetar()
                        return 0
                    
                if btn_Config_AbrirColisao.collidepoint(event.pos):
                    flag_menu_config_aberto = True
                    log("Abrindo Menu")
                elif btn_Config_FecharColisao.collidepoint(event.pos):
                    flag_menu_config_aberto = False
                    log("Fechando Menu")

            elif(cena == 3):
                portaBanheiroColisao = pygame.Rect(porta_banheiro)
                piaColisao = pygame.Rect(pia)
                privadaColisao = pygame.Rect(privada)
                btn_Config_AbrirColisao            = pygame.Rect(btnMenu_Config)
                btn_Config_FecharColisao           = pygame.Rect(box_menu_fechar)
                btn_Config_menu_SemSomColisao      = pygame.Rect(box_menu_SemSom)
                btn_Config_menu_ComSomColisao      = pygame.Rect(box_menu_ComSom)
                btn_menu_VoltarTelaInicialColisao  = pygame.Rect(btn_menu_VoltarTelaInicial)  

                if(flag_menu_config_aberto == False):
                    if portaBanheiroColisao.collidepoint(event.pos):
                        
                        if(lavar >= 3):
                            som_clique.play()
                            bolha,torneira,secar = False,False,False
                            log("Voltando para cozinha")
                            if(x < 4):
                                return cena-1
                            else:
                                return cena+3
                        else:
                            som_erro.play()
                            log("Você ainda precisa lavar as mãos")
                    
                    if piaColisao.collidepoint(event.pos):
                        if(lavar < 3):
                            som_clique.play()
                            log("Acessou a torneira")
                            return cena+1
                        else:
                            som_erro.play()
                            log("Você não precisa lavar as mãos")

                    elif privadaColisao.collidepoint(event.pos):
                        if(comida_full == False and bebida_full == False):
                            som_erro.play()
                            log("Você não precisa acessar fazer alguma necessidade")
                        else:
                            som_clique.play()
                            log("Acessou o vaso sanitário")
                            return cena+2
                else:
                    if btn_Config_menu_SemSomColisao.collidepoint(event.pos):
                        flag_cena_song = False
                    elif btn_Config_menu_ComSomColisao.collidepoint(event.pos):
                        flag_cena_song = True
                    elif btn_menu_VoltarTelaInicialColisao.collidepoint(event.pos):
                        flag_menu_config_aberto = False
                        som_background0.play(loops = -1)
                        som_background2.stop()
                        return 0
                    
                if btn_Config_AbrirColisao.collidepoint(event.pos):
                    flag_menu_config_aberto = True
                elif btn_Config_FecharColisao.collidepoint(event.pos):
                    flag_menu_config_aberto = False                
                
            elif(cena == 4):
                btn_Config_AbrirColisao = pygame.Rect(btnMenu_Config)
                btn_Config_FecharColisao = pygame.Rect(box_menu_fechar)
                btn_Config_menu_SemSomColisao = pygame.Rect(box_menu_SemSom)
                btn_Config_menu_ComSomColisao = pygame.Rect(box_menu_ComSom)
                btn_menu_VoltarTelaInicialColisao = pygame.Rect(btn_menu_VoltarTelaInicial)  
                btnVoltarColisao = pygame.Rect(Btn_Voltar)
                torneiraDesligadaColisao = pygame.Rect(torneira_desligada)
                torneiraLigadaColisao = pygame.Rect(torneira_ligada)
                toalhaColisao = pygame.Rect(toalha)
                espelhoColisao = pygame.Rect(espelho)
                sabaoColisao = pygame.Rect(sabao)
                
            
                if(flag_menu_config_aberto == False):
                    if btnVoltarColisao.collidepoint(event.pos):
                        bolha,torneira,secar = False,False,False
                        som_torneira.stop()
                        som_sabao.stop()
                        som_toalha.stop()
                        log("Voltando ao banheiro")
                        return cena-1

                    if torneira == False:
                        if torneiraDesligadaColisao.collidepoint(event.pos):
                            som_torneira.play()
                            lavar += 1
                            torneira = True
                            log("Abriu a torneira")
                    else:
                        if torneiraLigadaColisao.collidepoint(event.pos):
                            som_torneira.stop()
                            torneira = False
                            log("Fechou a torneira")

                    if bolha == False:
                        if sabaoColisao.collidepoint(event.pos):
                            som_sabao.play()
                            lavar += 1
                            log("Ensaboou as mãos")
                            bolha = True
                            anim_maos = 4

                    if secar == False:
                        if toalhaColisao.collidepoint(event.pos):
                            som_toalha.play()
                            lavar = lavar + 1
                            log("Secou as mãos")
                            secar = True
                           
                else:
                    if btn_Config_menu_SemSomColisao.collidepoint(event.pos):
                        flag_cena_song = False
                        log("Desligando Som")
                    elif btn_Config_menu_ComSomColisao.collidepoint(event.pos):
                        flag_cena_song = True
                        log("Ligando Som")
                    elif btn_menu_VoltarTelaInicialColisao.collidepoint(event.pos):
                        flag_menu_config_aberto = False
                        som_background0.play(loops = -1)
                        som_background2.stop()
                        som_torneira.stop()
                        log("Voltando para Tela Inicial")
                        resetar()
                        return 0
                    
                if btn_Config_AbrirColisao.collidepoint(event.pos):
                    flag_menu_config_aberto = True
                    log("Abrindo Menu")
                elif btn_Config_FecharColisao.collidepoint(event.pos):
                    flag_menu_config_aberto = False
                    log("Fechando Menu")                    

            elif(cena == 5):
                btn_Config_AbrirColisao = pygame.Rect(btnMenu_Config)
                btn_Config_FecharColisao = pygame.Rect(box_menu_fechar)
                btn_Config_menu_SemSomColisao = pygame.Rect(box_menu_SemSom)
                btn_Config_menu_ComSomColisao = pygame.Rect(box_menu_ComSom)
                btn_menu_VoltarTelaInicialColisao = pygame.Rect(btn_menu_VoltarTelaInicial)  
                btnVoltarColisao = pygame.Rect(Btn_Voltar)
                vasoFechadoColisao = pygame.Rect(vaso_fechado)
                papelColisao = pygame.Rect(papel)
                xixiIconColisao = pygame.Rect(xixi_icon)
                cocoIconColisao = pygame.Rect(coco_icon)
                alavancaColisao = pygame.Rect(alavanca)

                if(flag_menu_config_aberto == False):                
                    if btnVoltarColisao.collidepoint(event.pos):
                        if comida_full == False and bebida_full == False and switch == True and limpar == False:
                            som_clique.play()
                            som_descarga.stop()
                            rasgar,tampa,descarga,switch = False,False,False,False
                            log("Voltando ao banheiro")
                            return cena-2
                        else:
                            som_erro.play()
                            log("Você não fez tudo que devia")

                    if vasoFechadoColisao.collidepoint(event.pos):
                        if tampa == False:
                            som_clique.play()
                            log("Levantou a tampa")
                            tampa = True

                    if papelColisao.collidepoint(event.pos):
                        if limpar == True:
                            som_papel.play()
                            log("Puxou o papel higiênico")
                            rasgar = True
                            limpar = False
                        else:
                            som_erro.play()
                            log("Você não precisa se limpar")

                    if alavancaColisao.collidepoint(event.pos):
                        som_clique.play()                   
                        if switch == False:
                            if comida_full == True or bebida_full == True:
                                som_erro.play()
                                log("Você não precisa dar descarga")
                            else:
                                som_xixi.stop()
                                som_coco.stop()
                                som_descarga.play()                               
                                log("Você deu descarga")
                                switch = True
                            
                        if descarga == True:
                            descarga = False

                    if xixiIconColisao.collidepoint(event.pos):
                        if bebida_full == False:
                                som_erro.play()
                                log("Você não precisa fazer xixi")
                        else:
                            if(tampa == True):
                                som_xixi.play()
                                bebida_full = False
                                x += 1
                                lavar = 0
                                box_necessidades_sede_anim = 0
                                log("Você fez xixi")
                                descarga = True
                                if(sexo_Escolhido == "feminino"):
                                    limpar = True
                            else:
                                som_erro.play()
                                log("Abra a tampa do vaso")

                    if cocoIconColisao.collidepoint(event.pos):
                        if comida_full == False:
                                som_erro.play()
                                log("Você não precisa fazer cocô")
                        else:
                            if(tampa == True):
                                som_coco.play()
                                comida_full = False
                                x += 1
                                lavar = 0
                                box_necessidades_comida_anim = 0
                                log("Você fez cocô")
                                descarga = True
                                limpar = True
                            else:
                                som_erro.play()
                                log("Abra a tampa do vaso")
                        
                else:
                    if btn_Config_menu_SemSomColisao.collidepoint(event.pos):
                        flag_cena_song = False
                        log("Desligando Som")
                    elif btn_Config_menu_ComSomColisao.collidepoint(event.pos):
                        flag_cena_song = True
                        log("Ligando Som")
                    elif btn_menu_VoltarTelaInicialColisao.collidepoint(event.pos):
                        flag_menu_config_aberto = False
                        som_background0.play(loops = -1)
                        som_background2.stop()
                        som_descarga.stop()
                        log("Voltando para Tela Inicial")
                        resetar()
                        return 0
                    
                if btn_Config_AbrirColisao.collidepoint(event.pos):
                    flag_menu_config_aberto = True
                    log("Abrindo Menu")
                elif btn_Config_FecharColisao.collidepoint(event.pos):
                    flag_menu_config_aberto = False
                    log("Fechando Menu")                 
            elif(cena == 6):
                btnCreditosColisao = pygame.Rect(creditos2)
                btnSairColisao = pygame.Rect(sair2)
                btnPausarSomColisao = pygame.Rect(Btn_RemoverSom)
                btnContinuarSomColisao = pygame.Rect(Btn_AtivarSom)
                
                if btnCreditosColisao.collidepoint(event.pos):
                    log("Créditos")
                    som_clique.play()
                    return cena+1

                elif btnSairColisao.collidepoint(event.pos):
                    log("Sair")
                    som_clique.play()
                    pygame.quit()
                    sys.exit()
                    
                elif btnPausarSomColisao.collidepoint(event.pos):
                    flag_cena_song = False
                elif btnContinuarSomColisao.collidepoint(event.pos):
                    flag_cena_song = True

            elif(cena == 7):
                btnVoltarColisao = pygame.Rect(Btn_Voltar)

                if btnVoltarColisao.collidepoint(event.pos):
                    return cena-7
           
    return cena

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("PrismBaby - Alpha v1.0")
running = True
flag_cena_song = True
atual = 0
som_background0.play(loops = -1)

log("Iniciando o Jogo.")
log("Iniciando o Jogo..")
log("Iniciando o Jogo...")

while running:
    if flag_cena_song == False:
        pygame.mixer.pause()
    else:
        pygame.mixer.unpause()

    Exibir(atual)
    atual = Acoes(atual)
    pygame.display.update()
    pygame.display.flip()

