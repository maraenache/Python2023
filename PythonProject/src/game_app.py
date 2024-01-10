import pygame
import os

from src.game_controller import GameTableController
from src.constants import *


class GameApp(object):
    def __init__(self, instant_victory):
        """
        Initializeaza obiectul GameApp ce contine suprafetele/imaginile pt fundal, logo, carti
        :param instant_victory:specifica daca e activat instant_victory
        """

        self.main_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        pygame.init()
        pygame.display.set_caption("Solitaire")

        logo = pygame.image.load("%s/img/app_logo.png" % self.main_path)
        pygame.display.set_icon(logo)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.game_background_surface = None

        self.restart_tex = None
        self.restart_highlight_tex = None

        self.card_surfaces = {}
        self.initialize_surfaces()

        self.game_table_controller = GameTableController(self.card_surfaces, instant_victory)

        self.mouse_held = False
        self.mouse_pos = (0, 0)

        self.restart_button = pygame.Rect(RESTART_BUTTON_POSITION, RESTART_BUTTON_SIZE)

    def handle_input(self):
        """
         Gestioneaza input-ul utilizatorului pentru joc.
         Prin bucla care parcurge toate evenimentele pygame, se verifica daca evenimentul curent este de tip
        QUIT (inchidere fereastra). In caz afirmativ, functia returneaza valoarea 1, semnaland dorinta de inchidere a jocului.
        Altfel, se apeleaza functia handle_mouse_input pentru gestionarea input-ului de la mouse.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            else:
                self.handle_mouse_input(event)

    def handle_mouse_input(self, event):
        """
        Gestioneaza input-ul de la mouse pentru joc.
        Verifica tipul evenimentului de la mouse și prelucrează input-ul în consecință.
        Daca evenimentul este de tip MOUSEBUTTONDOWN (apasare buton mouse), se verifică daca butonul apasat este cel
        stâng și dacă nu este deja apăsat, semnalând astfel începerea apăsării mouse-ului.
        Daca evenimentul este de tip MOUSEBUTTONUP (ridicare buton mouse), se verifică daca butonul ridicat este cel
        stâng și dacă a fost apăsat anterior, semnalând astfel eliberarea butonului mouse-ului.
        :param event: Evenimentul de la mouse preluat de la pygame.
        """
        self.mouse_pos = pygame.mouse.get_pos()
        self.game_table_controller.mouse_pos = self.mouse_pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.mouse_held:  # Left mouse pressed
                self.mouse_held = True
                self.game_table_controller.mouse_clicked()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.mouse_held:  # Left mouse released
                self.mouse_held = False
                if self.restart_button.collidepoint(self.mouse_pos):
                    self.game_table_controller.restart_game()
                else:
                    self.game_table_controller.mouse_released()

    def start_game(self):
        """
        Stabileste o bucla continua pentru executia jocului(ce mentine ferestra pygame deschisa),
        unde se verifica input-ul utilizatorului prin apelul functiei handle_input.
        Daca input-ul indica dorinta de inchidere a jocului (codul 1),
        se iese din bucla, altfel se continua desenarea starii jocului prin apelul functiei draw_game.
        """
        running = True
        while running:
            if self.handle_input() == 1:
                running = False
            self.draw_game()

    def draw_game(self):
        """
        Deseneaza starea curenta a jocului pe ecran
        Verifica daca jucatorul a castigat sau daca jocul a fost desenat cel putin o data. Daca nu, se afiseaza
        fundalul jocului.
        Daca cursorul se afla deasupra butonului de repornire, se afiseaza versiunea evidentiata
        a butonului, in caz contrar, se afiseaza versiunea obisnuita.
        De asemenea, se deseneaza tabla de joc folosind obiectul game_table_controller.

        """
        if not self.game_table_controller.player_won or not self.game_table_controller.drawn_once:
            self.screen.blit(self.game_background_surface, (0, 0))
        if self.restart_button.collidepoint(self.mouse_pos):
            self.screen.blit(self.restart_highlight_tex, self.restart_button.topleft)
        else:
            self.screen.blit(self.restart_tex, self.restart_button.topleft)
            self.game_table_controller.draw_board(self.screen)

        pygame.display.flip()  # actualizez fundalul

    def initialize_surfaces(self):
        """
        Initializeaza suprafetele necesare pentru desenarea elementelor grafice ale jocului.
        Incarca imaginile necesare pentru fundalul jocului, butonul de repornire, suprafata placeholder-ului
        cartii, spatele cartii si seturile de carti cu inima, romb, trefla si frunza, redimensionandu-le la
        dimensiunea specificata in constanta CARD_DIMENSION. Aceste suprafete sunt stocate in dictionarul
        card_surfaces pentru a fi utilizate ulterior in desenarea elementelor jocului.
        """
        self.game_background_surface = pygame.image.load("%s/img/background.png" % self.main_path)

        self.restart_tex = pygame.transform.scale(pygame.image.load("%s/img/restart2.jpg" % self.main_path),
                                                  RESTART_BUTTON_SIZE)
        self.restart_highlight_tex = pygame.transform.scale(
            pygame.image.load("%s/img/restart.png" % self.main_path), RESTART_BUTTON_SIZE)

        # surfaces - dictionar de poze pt card
        self.card_surfaces["placeholder"] = pygame.image.load(
            "%s/img/card_surfaces/placeholder_surface.png" % self.main_path)
        self.card_surfaces["card_back"] = pygame.image.load(
            "%s/img/card_surfaces/card_back_background_surface.png" % self.main_path)
        self.card_surfaces["deck"] = self.card_surfaces["card_back"]

        cards_set = "%s/img/card_surfaces/cards_set" % self.main_path
        heart_cards_surfaces = {}
        diamond_cards_surfaces = {}
        club_cards_surfaces = {}
        spade_cards_surfaces = {}

        try:
            for image_file in os.listdir(cards_set):
                if image_file.endswith(".png"):
                    new_tex = pygame.transform.scale(pygame.image.load(os.path.join(cards_set, image_file)),
                                                     CARD_DIMENSION)
                    filepath_split = image_file.split('_')
                    card_value = int(filepath_split[0])
                    card_color = filepath_split[1]
                    card_suit = filepath_split[2]

                    if card_color == 'b':
                        if card_suit == 'club':
                            club_cards_surfaces[card_value] = new_tex
                        elif card_suit == 'spade':
                            spade_cards_surfaces[card_value] = new_tex
                    elif card_color == 'r':
                        if card_suit == 'heart':
                            heart_cards_surfaces[card_value] = new_tex
                        elif card_suit == 'diamond':
                            diamond_cards_surfaces[card_value] = new_tex
                    else:
                        print("problem in game_app-> initialize surfaces")

            self.card_surfaces["heart_cards"] = heart_cards_surfaces
            self.card_surfaces["diamond_cards"] = diamond_cards_surfaces
            self.card_surfaces["club_cards"] = club_cards_surfaces
            self.card_surfaces["spade_cards"] = spade_cards_surfaces

        except ValueError as err:
            print("Error loading cards surfaces. %s" % err)
