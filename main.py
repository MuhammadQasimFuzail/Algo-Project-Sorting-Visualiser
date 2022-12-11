import pygame, sys
from button import Button
import random
import pygame
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sorts
from matplotlib.ticker import FormatStrFormatter
import subprocess

pygame.init()

SCREEN = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("Menu")

file_name = ''

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def sort_Main(method):

    h = open(file_name, 'r')
 
# Reading from the file
    content = h.readlines()
    
    # Variable for storing the sum
    a = 0
    A=[]
    # Iterating through the content
    # Of the file
    for line in content:
        
        for line in content:

            fields = line.strip().split()
    random.shuffle(fields)
    res = [eval(i) for i in fields]
    N=len(fields)
    A=res
    print(len(A))
    print(A)


    # Get appropriate generator to supply to matplotlib FuncAnimation method.
    if method == "b":
        title = "Bubble sort"
        generator = sorts.bubblesort(A)
    elif method == "i":
        title = "Insertion sort"
        generator = sorts.insertionsort(A)
    elif method == "h":
        title = "Heap sort"
        generator = sorts.heapSort(A)
    elif method == "r":
        title = "Radix sort"
        generator = sorts.radixSort(A)
    elif method == "c":
        title = "Count sort"
        generator = sorts.countingSort(A)
    elif method == "m":
        title = "Merge sort"
        generator = sorts.mergesort(A, 0, N - 1)
    elif method == "q":
        title = "Quicksort"
        generator = sorts.quicksort(A, 0, N - 1)
    elif method == "hq":
        title = "Hybrid Quicksort"
        generator = sorts.hybrid_quick_sort(A, 0, N-1)
    elif method == "cs":
        title = "New Counting Sort"
        generator = sorts.last_algo(A,0,N)
    elif method == "bs":
        title = "Bucket sort"
        generator = sorts.bucketSort(A)
    else:
        title = "Selection sort"
        generator = sorts.selectionsort(A)

    # Initialize figure and axis.
    fig, ax = plt.subplots()

    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax.set_title(title)

 
    bar_rects = ax.bar(range(len(A)), A, align="edge")

    ax.set_xlim(0, N)
    ax.set_ylim(0, int(max(A)+5))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

   
    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        if title=='Radix sort':
            text.set_text("")        
        else:
            text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)
    plt.get_current_fig_manager().full_screen_toggle() # toggle fullscreen mode
    plt.show()

def play():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

      
      
        button1 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 100), 
                            text_input="INSERTION", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        button2 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 200), 
                            text_input="BUBBLE", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        button3 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 300), 
                            text_input="MERGE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        button4 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 400), 
                            text_input="HEAP", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        button5 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 500), 
                            text_input="QUICK", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        button6 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 600), 
                            text_input="NEXT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")




        for button in [button1, button2, button3,button4,button5,button6]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.checkForInput(MENU_MOUSE_POS):
                    sort_Main('i')
                if button2.checkForInput(MENU_MOUSE_POS):
                    sort_Main('b')
                if button3.checkForInput(MENU_MOUSE_POS):
                    sort_Main('m')
                if button4.checkForInput(MENU_MOUSE_POS):
                    sort_Main('h')
                if button5.checkForInput(MENU_MOUSE_POS):
                    sort_Main('q')
                if button6.checkForInput(MENU_MOUSE_POS):
                    page2()

        pygame.display.update()


def page2():
    while True:

        #print(len(A))
        #print(A)

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

      

        button1 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 100), 
                            text_input="RADIX", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        button2 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 200), 
                            text_input="BUCKET", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        button3 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 300), 
                            text_input="COUNTING", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        button4 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 400), 
                            text_input="7.4.5", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        button5 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 500), 
                            text_input="8.2.4", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        button6 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 600), 
                            text_input="BACK", font=get_font(40), base_color="#d7fcd4", hovering_color="White")



        for button in [button1, button2, button3,button4,button5,button6]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.checkForInput(MENU_MOUSE_POS):
                    sort_Main('r')
                if button2.checkForInput(MENU_MOUSE_POS):
                    sort_Main('bs')
                if button3.checkForInput(MENU_MOUSE_POS):
                    sort_Main('c')
                if button4.checkForInput(MENU_MOUSE_POS):
                    sort_Main('hq')
                if button5.checkForInput(MENU_MOUSE_POS):
                    takeInputLwBound()
                if button6.checkForInput(MENU_MOUSE_POS):
                    main_menu()


        pygame.display.update()
    
def options():
    subprocess.call(["xdg-open", "time.pdf"])
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(25).render("Time complexity document launched", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def dispAns(ans):
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(20).render(str(ans)+" numbers fall in the range entered", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def takeInputUpBound(lwBound):
    base_font = pygame.font.Font(None, 32)
    user_text = ''

    # create rectangle
    input_rect = pygame.Rect(200, 200, 140, 32)

    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')
    
    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    
    active = False
    h = open(file_name, 'r')
 
    # Reading from the file
    content = h.readlines()
        
        # Variable for storing the sum
    a = 0
    A=[]
        # Iterating through the content
        # Of the file
    for line in content:
            
        for line in content:

            fields = line.strip().split()
    random.shuffle(fields)
    res = [eval(i) for i in fields]
    N=len(fields)
    A=res

    
    while True:
        SCREEN.fill("white")
        SCREEN.blit(BG, (0, 0))


        PROMPT_TEXT = get_font(45).render("Enter upper bound", True, "White")
        PROMPT_RECT = PROMPT_TEXT.get_rect(center=(640, 240))
        SCREEN.blit(PROMPT_TEXT, PROMPT_RECT)
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        input_rect = pygame.Rect(470, 300, 330, 32) 


        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_NEXT = Button(image=None, pos=(640, 560), 
                            text_input="NEXT", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_NEXT.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_NEXT.update(SCREEN)        
        for event in pygame.event.get():
        
        # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:

                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_NEXT.checkForInput(OPTIONS_MOUSE_POS):
                    if user_text!='':
                        print(int(user_text))
                        a = sorts.last_algo(A,lwBound,int(user_text))
                        dispAns(a)
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
            
            # Check for backspace
                if event.key == pygame.K_BACKSPACE:
            
                    user_text = user_text[:-1]
        
                else:
                    user_text += event.unicode
            
        #SCREEN.fill((255, 255, 255))

        pygame.draw.rect(SCREEN, "Grey", input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))

        SCREEN.blit(text_surface, (input_rect.x+30, input_rect.y+5))

        input_rect.w = max(100, text_surface.get_width()+10)

        pygame.display.flip()


def takeInputLwBound():
    base_font = pygame.font.Font(None, 32)
    user_text = ''

    # create rectangle
    input_rect = pygame.Rect(200, 200, 140, 32)

    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')
    
    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    
    active = False
    
    while True:
        SCREEN.fill("white")
        SCREEN.blit(BG, (0, 0))

        PROMPT_TEXT = get_font(45).render("Enter lower bound", True, "white")
        PROMPT_RECT = PROMPT_TEXT.get_rect(center=(640, 240))
        SCREEN.blit(PROMPT_TEXT, PROMPT_RECT)
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        input_rect = pygame.Rect(470, 300, 330, 32) 


        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_NEXT = Button(image=None, pos=(640, 560), 
                            text_input="NEXT", font=get_font(75), base_color="white", hovering_color="Green")

        OPTIONS_NEXT.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_NEXT.update(SCREEN)        
        for event in pygame.event.get():
        
        # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:

                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_NEXT.checkForInput(OPTIONS_MOUSE_POS):
                    if user_text!='':
                        print(int(user_text))
                        takeInputUpBound(int(user_text))
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
            
            # Check for backspace
                if event.key == pygame.K_BACKSPACE:
            
                    user_text = user_text[:-1]
        
                else:
                    user_text += event.unicode
            
        #SCREEN.fill((255, 255, 255))

        pygame.draw.rect(SCREEN, "Grey", input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))

        SCREEN.blit(text_surface, (input_rect.x+30, input_rect.y+5))

        input_rect.w = max(100, text_surface.get_width()+10)

        pygame.display.flip()



def inputFileName():
    base_font = pygame.font.Font(None, 32)
    user_text = ''

    # create rectangle
    input_rect = pygame.Rect(200, 200, 140, 32)

    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')
    
    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    
    active = False
    
    while True:
        SCREEN.fill("white")
        SCREEN.blit(BG, (0, 0))

        PROMPT_TEXT = get_font(45).render("Enter file name", True, "white")
        PROMPT_RECT = PROMPT_TEXT.get_rect(center=(640, 240))
        SCREEN.blit(PROMPT_TEXT, PROMPT_RECT)
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        input_rect = pygame.Rect(470, 300, 330, 32) 



        OPTIONS_NEXT = Button(image=None, pos=(640, 560), 
                            text_input="NEXT", font=get_font(75), base_color="white", hovering_color="Green")

        OPTIONS_NEXT.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_NEXT.update(SCREEN)        
        for event in pygame.event.get():
        
        # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:


                if OPTIONS_NEXT.checkForInput(OPTIONS_MOUSE_POS):
                    if user_text!='':
                        global file_name
                        file_name=user_text
                        main_menu()
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
            
            # Check for backspace
                if event.key == pygame.K_BACKSPACE:
            
                    user_text = user_text[:-1]
        
                else:
                    user_text += event.unicode
            
        #SCREEN.fill((255, 255, 255))

        pygame.draw.rect(SCREEN, "Grey", input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))

        SCREEN.blit(text_surface, (input_rect.x+30, input_rect.y+5))

        input_rect.w = max(100, text_surface.get_width()+10)

        pygame.display.flip()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Sorting Visualiser", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="Visualiser", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="Time Complexity", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

inputFileName()