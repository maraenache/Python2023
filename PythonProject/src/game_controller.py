import pygame

from src.card_factory import Deck, BaseHolder, TopLeftHolder, TopRightHolder, MouseHolder
from src.constants import *


class GameTableController(object):
    def __init__(self, card_surfaces, instant_victory):
        self.placeholder_surface = card_surfaces["placeholder"]
        self.instant_victory = instant_victory
        self.deck_pos = (BASE_ROW_XY[0], TOP_ROW_Y)  # setul de carti la 200,20
        self.mouse_pos = (0, 0)

        self.base_level_holders = []
        self.top_right_level_holders = []
        self.top_left_level_holder = None

        self.base_level_horizontals = []  # pozitiile de sus x1___x2 pt cele 7 de jos
        self.top_right_level_horizontals = []  # poz de sus pt fiecare din cele 4 de sus dreapta

        self.mouse_holder = MouseHolder()

        self.initialize_holders()
        self.deck = Deck(self.deck_pos, self.top_left_level_holder, self.base_level_holders,
                         self.top_right_level_holders, card_surfaces, instant_victory)
        self.player_won = instant_victory
        self.drawn_once = False
        self.imported_font = pygame.font.Font("Starborn.ttf", 50)

    def display_win_message(self, screen):
        text_color = (253, 218, 13)  # albastru
        text = "You won! Congrats!"
        text_surface = self.imported_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 250))
        screen.blit(text_surface, text_rect)

    def mouse_clicked(self):
        if self.player_won:
            return
        # Bottom row
        if self.mouse_pos[1] > BASE_ROW_XY[1]:
            for i in range(len(self.base_level_horizontals)):
                if self.base_level_horizontals[i][0] < self.mouse_pos[0] < self.base_level_horizontals[i][1]:
                    self.base_level_holders[i].grabCard(self.mouse_pos, self.mouse_holder)
                    break

        # Top right row
        elif self.mouse_pos[0] > BASE_ROW_XY[0] + 3 * (CARD_SPACING + CARD_DIMENSION[0]):
            for i in range(len(self.top_right_level_horizontals)):
                if self.top_right_level_horizontals[i][0] < self.mouse_pos[0] < self.top_right_level_horizontals[i][1]:
                    self.top_right_level_holders[i].grabCard(self.mouse_pos, self.mouse_holder)
                    break
        else:
            if self.deck.in_bounds(self.mouse_pos):
                self.deck.clicked()
            else:
                tl_holder_width = CARD_DIMENSION[0] + min(2, len(self.top_left_level_holder.cards)) * \
                                  TOP_LEFT_HOLDER_OFFSET[0]
                if self.top_left_level_holder.position[0] < self.mouse_pos[0] < self.top_left_level_holder.position[
                    0] + tl_holder_width \
                        and TOP_ROW_Y < self.mouse_pos[1] < TOP_ROW_Y * CARD_DIMENSION[1]:
                    self.top_left_level_holder.grabCard(self.mouse_pos, self.mouse_holder)

    def mouse_released(self):
        if self.player_won:
            return

        if len(self.mouse_holder.cards) == 0:
            return 0
        # Position to check if card intersects with holder
        bottom_card = self.mouse_holder.cards[0]
        card_contact_point = (
            self.mouse_pos[0] + self.mouse_holder.mouse_relative_position[0] + int(CARD_DIMENSION[0] / 2),
            self.mouse_pos[1] + self.mouse_holder.mouse_relative_position[1] + int(CARD_DIMENSION[1] / 2))
        new_holder = check_win = False

        # Bottom row
        if self.mouse_pos[1] > BASE_ROW_XY[1]:
            for i in range(len(self.base_level_horizontals)):
                if self.base_level_horizontals[i][0] < card_contact_point[0] < self.base_level_horizontals[i][1]:
                    new_holder = self.base_level_holders[i].add_card(bottom_card, player_action=True,
                                                                     contact_point=card_contact_point)
                    # Top right row
        elif self.mouse_pos[0] > BASE_ROW_XY[0] + 3 * (CARD_SPACING + CARD_DIMENSION[0]):
            for i in range(len(self.top_right_level_horizontals)):
                if self.top_right_level_horizontals[i][0] < card_contact_point[0] < self.top_right_level_horizontals[i][
                    1]:
                    new_holder = self.top_right_level_holders[i].add_card(bottom_card, player_action=True,
                                                                          contact_point=card_contact_point)
                    check_win = True
        last_holder = self.mouse_holder.last_holder
        if not new_holder:  # put cards from mouse holder back to last holder
            self.mouse_holder.transfer_cards(last_holder)
        else:  # put cards from mouse holder to new holder
            self.mouse_holder.transfer_cards(new_holder)
            if len(last_holder.cards) > 0:
                last_holder.cards[-1].revealed = True

        if check_win:
            self.check_win()

    # daca toate holderele din dreapta au lungime 13 carti a castigat
    def check_win(self):
        for holder in self.top_right_level_holders:
            if len(holder.cards) != 13:
                return
        self.player_won = True

    def initialize_holders(self):
        """
        Aceasta functie initializeaza holder-ele pentru jocul Solitaire.Initial face un pentru cele 7 holdere de la base
        si cele 4 top right holdere, vor fi desenate deasupra la ult 4 base holders

        :return:
        """
        for i in range(7):

            new_br_pos = (
                BASE_ROW_XY[0] + i * (CARD_SPACING + CARD_DIMENSION[0]), BASE_ROW_XY[1])  # 200+i*(20+98), 180
            self.base_level_horizontals.append((new_br_pos[0], (new_br_pos[0] + CARD_DIMENSION[0])))
            self.base_level_holders.append(BaseHolder(new_br_pos, self.placeholder_surface))
            if i < 4:
                new_tr_pos = (BASE_ROW_XY[0] + (i + 3) * (CARD_SPACING + CARD_DIMENSION[0]), TOP_ROW_Y)
                # 200+(i+3)(2-+89), 20
                self.top_right_level_horizontals.append((new_tr_pos[0], (new_tr_pos[0] + CARD_DIMENSION[0])))
                self.top_right_level_holders.append(TopRightHolder(new_tr_pos, self.placeholder_surface))
                self.top_left_level_holder = TopLeftHolder(
                    (BASE_ROW_XY[0] + CARD_SPACING + CARD_DIMENSION[0], TOP_ROW_Y),
                    self.placeholder_surface)

    def restart_game(self):
        self.reset_holders()
        self.deck.shuffle_cards()
        self.deck.deal_cards()
        self.drawn_once = False
        if not self.instant_victory:
            self.player_won = False

    def reset_holders(self):
        for holder in self.base_level_holders + self.top_right_level_holders:
            holder.cards = []

        self.top_left_level_holder.cards = []
        self.mouse_holder.cards = []

    def draw_board(self, screen):
        if self.player_won and self.drawn_once:
            self.display_win_message(screen)
            pygame.display.flip()
            return
        self.drawn_once = True
        for holder in self.base_level_holders + self.top_right_level_holders:
            holder.drawCards(screen)
        one_held = len(self.mouse_holder.cards) > 0 and self.mouse_holder.last_holder == self.top_left_level_holder
        self.top_left_level_holder.drawCards(screen, one_held)

        self.deck.draw(screen)
        # Move and draw mouse holder
        if len(self.mouse_holder.cards) > 0:
            self.mouse_holder.drawCards(screen, position=self.mouse_pos)
