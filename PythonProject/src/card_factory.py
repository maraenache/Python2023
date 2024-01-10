import random
import sys
from constants import *


class Card(object):
    def __init__(self, card_surfaces, suit, value):
        """
        Initializeaza un obiect de tip carte
        cu variabilele referitoare la suorafata cartii simbolul si valoarea si daca e sau nu afisata
        :param card_surfaces: Lista de suprafete pentru fata si spatele cartii
        :param suit: simbolul cartii(ex romb)
        :param value: un numar de la 1 la 13, valoarea cartii
        """
        self.card_face_surface = card_surfaces[0]
        self.card_back_surface = card_surfaces[1]
        self.suit = suit
        self.value = value
        self.revealed = False

    def draw(self, screen, position):
        """
        Deseneaza cartea pe ecran la o anumita pozitie,
        daca e revealed, ii deseneaza fata, altfel spatele
        :param screen: suprafata pe care desenam
        :param position: pozitia la care desenam
        """
        if self.revealed:
            screen.blit(self.card_face_surface, position)
        else:
            screen.blit(self.card_back_surface, position)

    def __str__(self):
        """
        Reprezentarea sub forma de sir de caractere a cartii, va fi de ex 2 diamond
        """
        return "%d %s" % (self.value, self.suit.lower().capitalize())


class Deck(object):
    def __init__(self, position, deal_holder, base_level_holders, top_right_level_holders, card_surfaces,
                 instant_victory=False):

        self.position = position
        self.deal_holder = deal_holder
        self.base_level_holders = base_level_holders
        self.top_right_level_holders = top_right_level_holders

        self.card_back_surface = card_surfaces["card_back"]
        self.placeholder_surface = card_surfaces["placeholder"]
        self.heart_cards_surfaces = card_surfaces["heart_cards"]
        self.diamond_cards_surfaces = card_surfaces["diamond_cards"]
        self.club_cards_surfaces = card_surfaces["club_cards"]
        self.spade_cards_surfaces = card_surfaces["spade_cards"]
        self.deck_surface = card_surfaces["deck"]
        self.reveal_one_by_one = False
        self.instant_victory = instant_victory

        self.cards = []
        self.shuffle_cards()
        self.deal_cards()

    def shuffle_cards(self):
        """
        Amesteca cartile din pachetul de joc.

        Genereaza un nou pachet de carti si atribuie fiecarei carti o suprafata corespunzatoare in functie
        de culoare si figura. Daca modul instant_victory este activat, cartile sunt puse in ordine.
        Altfel, se amesteca pachetul prin extragerea aleatorie a cartilor din pachetul initial.
        """
        new_deck = []
        value = 1
        suit_counter = 0
        for i in range(52):
            suit = CARD_SUITS[suit_counter]
            if suit_counter == 0:
                card_face_surface = self.heart_cards_surfaces[value]
            elif suit_counter == 1:
                card_face_surface = self.diamond_cards_surfaces[value]
            elif suit_counter == 2:
                card_face_surface = self.club_cards_surfaces[value]
            else:
                card_face_surface = self.spade_cards_surfaces[value]
            new_deck.append(Card([card_face_surface, self.card_back_surface], suit, value))

            suit_counter += 1  # pun o carte 1 de inima, dupa pun 1 de diamant, dupa 1 de trefla si frunza

            if suit_counter > 3:
                suit_counter = 0
                value += 1  # dupa ce am pus acelasi nr de fiecare forma, trec la urm nr

        if self.instant_victory:
            self.cards = new_deck  # sunt puse in ordine
            return

        self.cards = []
        while len(new_deck) > 0:  # le amestec, elimin pe rand cate una extrasa random si o pun in  cards
            random_card_position = random.randint(0, len(new_deck) - 1)
            self.cards.append(new_deck[random_card_position])
            del new_deck[random_card_position]

    def deal_cards(self):
        """
        Imparte cartile in functie de modul de joc.
        Daca modul instant_victory este activat, cartile sunt adaugate direct in cele 4 holdere din drapta sus
        Altfel cartile sunt distribuite in base_level_holders, conform cu regula jocului Solitaire
        """
        if self.instant_victory:  # le am ordonate si le pun direct in top right holders
            index = 0
            for card in self.cards:
                card.revealed = True
                self.top_right_level_holders[index].add_card(card)
                index += 1
                if index > 3:
                    index = 0
            return

        for i in range(-1, 6):  # -1,-2..5
            for j in range(6, i, -1):
                self.base_level_holders[j].add_card(self.cards[-1])
                self.cards = self.cards[:-1]

        for card_holder in self.base_level_holders:
            card_holder.cards[-1].revealed = True

    def clicked(self):
        """
        Proceseaza evenimentul de click pe deal holder.
        Se poate dezvalui doar cate o carte, sau se dezvaluie trei carti diferite
        Daca exista carti in deal holder, le dezvaluie si le adauga la self.cards (deck)
        self.cards-cele care n-au fost dezvaluite inca.
        In cazul in care pachetul contine carti, functia dezvaluie un numar de carti specificat de minimul dintre
        number_of_cards_revealed si cate sunt disponibile.
        Daca nu exista carti in pachetul principal, toate cartile revealed in deal holder sunt mutate inapoi in pachet.        """
        number_of_cards_revealed = 3
        if self.reveal_one_by_one:
            number_of_cards_revealed = 1

        if len(self.cards) > 0:
            for i in range(min(len(self.cards),
                               number_of_cards_revealed)):  # de la 0 la minimul dintre cate sunt si card count
                self.cards[i].revealed = True
                self.deal_holder.add_card(self.cards[i])
            self.cards = self.cards[
                         min(len(self.cards), number_of_cards_revealed):]  # restul de la min la sfarsit in deck
        else:
            for i in range(len(self.deal_holder.cards)):
                self.cards.append(self.deal_holder.cards[i])
            self.deal_holder.cards = []

    def in_bounds(self, mouse_pos):
        return self.position[0] < mouse_pos[0] < self.position[0] + CARD_DIMENSION[0] \
            and self.position[1] < mouse_pos[1] < self.position[1] + CARD_DIMENSION[1]

    def draw(self, screen):
        """
        Deseneaza pachetul din stanga sus pe ecran
        Daca exista carti in pachet, afiseaza suprafata spatele unei carti, altfel afiseaza o suprafata de asteptare
        """
        if len(self.cards) > 0:
            screen.blit(self.deck_surface, self.position)
        else:
            screen.blit(self.placeholder_surface, self.position)


class CardHolder(object):
    def __init__(self, position, placeholder):
        self.position = position
        self.placeholder_surface = placeholder
        self.cards = []
        self.offset = (0, 0)

    def add_card(self, card, player_action=False, contact_point=None):
        """
        Adauga o carte in card holder. (card-cartea care va fi adaugata)
        last_card_top_pos: reprezinta pozitia verticala(y-ul) a partii superioare a ultimei carti vizibile din holder,
        calculata in functie de pozitia holder-ului, offset-ul vertical al cartilor si numarul de carti vizibile
        :return: Returneaza card holder-ul daca adaugarea s-a realizat cu succes, altfel returneaza None.
        """
        if not player_action:
            self.cards.append(card)
            return

        if contact_point is None:
            sys.exit("in addCard: If player action; contact point arg must be not None")

        last_card_top_pos = self.position[1] + self.offset[1] * (len(self.cards) - 1) + 50
        # print(f"{last_card_top_pos, contact_point[1], last_card_top_pos + CARD_DIMENSION[1]}")
        if last_card_top_pos < contact_point[1] < last_card_top_pos + CARD_DIMENSION[1]:
            if self.check_suit_and_val(self.cards, card, lastCard=True):
                return self

        return None

    def check_suit_and_val(self, card1, card2):
        sys.exit("This function is overridden in the derived classes and is not intended for use in the base class.")

    def is_valid_parent_card(self, index):
        """
        Verifica daca cartea de la pozitia specificata (idx) este o carte parinte corecta
        print(len(self.cards))  # cate carti sunt in base holderul respectiv din care iau cartea

        :param index: Pozitia cartii in cartile holderului din care face parte
        :return: True daca cartea este un parinte valid, False in caz contrar.

        """
        prev_card = self.cards[index]
        for i in range(index + 1, len(self.cards)):
            if not self.check_suit_and_val(prev_card, self.cards[i]):
                return False
            prev_card = self.cards[i]
        return True

    def transfer_cards(self, target_holder, index=0):
        """
        realizeaza transferul de carti din holderul curent intr-un alt holder(target) specificat.
        Transferul incepe de la indexul specificat (default 0) si continua pana la finalul holderului curent.
        print("Trying to move", self.cards[index])-cartile pe care vreau sa le transfer
        adauga fiecare carte din holderul curent(cards) in target_holder si o sterge din holderul curent.
        si continua pana cand toate cartile de la indexul specificat sunt transferate
        print(len(self.cards))
        :param target_holder: holderul tinta in care se vor transfera cartile
        :param index: indexul de la care incepe transferul de carti
        """
        while len(self.cards) > index:
            target_holder.add_card(self.cards[index])
            del self.cards[index]

    def drawCards(self, screen):
        """
        deseneaza cartile dintr-un holder. Daca el nu contine nicio carte, se afiseaza o suprafata placeholder
        In caz contrar, fiecare carte din suport este afisata pe ecran, respectand pozitiile calculate in functie de offset
        :param screen: suparafata pe care desenam
        """
        if len(self.cards) == 0:
            screen.blit(self.placeholder_surface, self.position)
            return
        for i in range(len(self.cards)):
            self.cards[i].draw(screen, (self.position[0] + self.offset[0] * i, self.position[1] + self.offset[1] * i))


class BaseHolder(CardHolder):
    # subclasa a CardHolder
    def __init__(self, pos, placeholder):
        CardHolder.__init__(self, pos, placeholder)
        self.offset = BASE_HOLDER_OFFSET  # 0,30 ce e diferit de init de la card holder

    def grabCard(self, mouse_pos, mouse_holder):
        """
        permite utilizatorului sa ia o carte dintr un holder folosind pozitia mouse-ului.
        Functia parcurge toate cartile prezente in suport si verifica daca pozitia mouse-ului
        se afla deasupra unei carti care este dezvaluita.
        Daca da si cartea este un parinte valid conform regulilor jocului, atunci cartea este transferata
        in suportul de carti coresp mouse-ului.
        print("the parent is", self.cards[i], "si i e", i) # self.cards[i]-cartea pe care o apuc
        i al catalea brholder e, de la 0 la 6
        print("br gol e>>>", i)
        :param mouse_pos: Pozitia curenta a mouse-ului # print(mouse_pos[0],mouse_pos[1])
        :param mouse_holder: Obiectul care reprezinta suportul de carti al mouse-ului
        """
        for i in range(len(self.cards)):
            card_pos = (
                self.position[0], self.position[1] + self.offset[1] * i)  # +30*i, ca gen le pune din 30 in 30 pe y
            if i == len(self.cards) - 1:  # daca e ult carte o afisez
                height = CARD_DIMENSION[1]
            else:
                height = CARD_HOLDER_VERTICAL_OFFSET  # daca nu la restul fac varoffset care e 30

            if card_pos[1] < mouse_pos[1] < card_pos[1] + height and self.cards[i].revealed:
                if self.is_valid_parent_card(i):
                    self.transfer_cards(mouse_holder, i)
                    mouse_holder.mouse_relative_position = (card_pos[0] - mouse_pos[0], card_pos[1] - mouse_pos[1])
                    mouse_holder.last_holder = self
                return

    def check_suit_and_val(self, target_card, selected_card, lastCard=False):
        """
        verif daca o carte selectata poate fi plasata pe o alta carte tinta, respectand regulile jocului
        Functia are in vedere suit-ul (culoarea) si valoarea cartilor implicate.
        Se verifica daca suit-ul ambelor carti este diferit ca culoare (rosie vs. neagra).
        Se verifica daca valoarea cartii selectate este cu 1 mai mica decat valoarea cartii tinte
        target card e cu 1 mai mare decat selected
        initial target_card e target_holder_cards, dupa prin target_card = target_card[-1]  ramane cu ultima

        :param target_card: Cartea tinta pe care se doreste a fi plasata alta carte
        :param selected_card: Cartea selectata care se doreste a fi plasata
        :param lastCard: (optional) indica daca target_card este ultima carte din holder (default: False)
        """
        if lastCard:
            if len(target_card) == 0:
                return True
            target_card = target_card[-1]

        # check color of suit
        if target_card.suit in CARD_SUITS[:2] and selected_card.suit in CARD_SUITS[:2]:
            return False

        if target_card.suit in CARD_SUITS[2:4] and selected_card.suit in CARD_SUITS[2:4]:
            return False
        # culori dif=> check value
        if target_card.value != selected_card.value + 1:
            return False
        return True


class TopRightHolder(CardHolder):
    def __init__(self, pos, placeholder):
        CardHolder.__init__(self, pos, placeholder)
        self.offset = TOP_RIGHT_HOLDER_OFFSET

    def grabCard(self, mouse_pos, mouse_holder):
        """
        grab pt o carte din top right holder. dacă exista carti in holderul respectiv
        si daca poz mouse ului se afla in zona corespunzatoare suportului, atunci ultima carte din suport
        este adaugata in mouseholder, +informatii despre poz relativa a mouse ului

        :param mouse_pos:pozitia curenta a mouseului
        :param mouse_holder:holderul asociat pozitiei mouseului

        """
        if len(self.cards) <= 0:
            return

        if self.position[1] < mouse_pos[1] < self.position[1] + CARD_DIMENSION[1]:
            mouse_holder.add_card(self.cards[-1])
            mouse_holder.mouse_relative_position = (self.position[0] - mouse_pos[0], self.position[1] - mouse_pos[1])
            mouse_holder.last_holder = self
            del self.cards[-1]

    def check_suit_and_val(self, target_card, selected_card, lastCard=False):
        """
        verifica potrivirea dintre doua carti in top_right_holder (target si selected) in ceea ce priveste culoarea si
        valoarea lor. In mod implicit, functia compara cartile individual, dar atunci cand este setat parametrul
        optional lastCard ca True functia considera doar ultima carte dintr-un set de carti (target_card).
        Functia verifica daca cele doua carti au acelasi simbol si daca valoarea card1 este cu 1 mai mica decat valoarea
         selected_card
        :param target_card:cartea tinta pe care vreau sa o pun pe cea selected
        :param selected_card:A doua carte pentru comparare
        :param lastCard:Indicator daca trebuie comparata doar ultima carte dintr-un set de carti
        :return:True daca cartile se potrivesc si False in caz contrar.
        """
        if lastCard:
            if len(target_card) == 0:
                if selected_card.value == 1:
                    return True
                else:
                    return False
            target_card = target_card[-1]
        # check color of suit
        if target_card.suit != selected_card.suit:
            return False
        # check value
        if target_card.value != selected_card.value - 1:
            return False
        return True


class TopLeftHolder(CardHolder):
    def __init__(self, pos, placeholder):
        CardHolder.__init__(self, pos, placeholder)
        self.offset = TOP_LEFT_HOLDER_OFFSET

    def grabCard(self, mouse_pos, mouse_holder):
        """
         grab pt o carte din top left holder. verifica daca exista carti in holder, iar apoi verifica daca pozitia
         cursorului corespunde cu pozitia cartii superioare. In caz afirmativ, adauga cartea in holderul
         cursorului, actualizeaza pozitia relativa a cursorului si retine referinta la ultimul holder utilizat
         Functia verifica daca exista cel putin o carte in holder inainte de a proceda
         Se afiseaza maxim primele 3 carti din holder, iar comparatia pozitiei cursorului se face doar pentru cea mai
        de sus. Daca pozitia cursorului corespunde cu pozitia cartii superioare, aceasta este adaugata in holderul
         cursorului, iar apoi este eliminata din holderul curent.

        :param mouse_pos:pozitia mouse
        :param mouse_holder:holder asociat mouse/cursorului
        """
        if len(self.cards) <= 0:
            return
        cards_displayed = min(len(self.cards), 3)
        card_pos = (self.position[0] + self.offset[0] * (cards_displayed - 1), self.position[1])
        if card_pos[0] < mouse_pos[0] < card_pos[0] + CARD_DIMENSION[0]:
            mouse_holder.add_card(self.cards[-1])
            mouse_holder.mouse_relative_position = (card_pos[0] - mouse_pos[0], card_pos[1] - mouse_pos[1])
            mouse_holder.last_holder = self
            del self.cards[-1]

    def drawCards(self, screen, one_held):
        """
        deseneaza cartile din top left holder pe ecran.
        Verifica daca exista carti in holder si deseneaza un numar specific de carti,in functie de situatie.
        Daca nu exista carti in holder, se deseneaza un placeholder.
        Daca one_held este True, se deseneaza maxim prima carte.
        Daca one_held este False, se deseneaza maxim primele 3 carti.
        Desenarea se face in functie de pozitia si offset-ul fiecarei carti in holder.
        :param screen:Ecranul Pygame pe care se realizeaza desenarea
        :param one_held:Indicator care specifica daca trebuie desenata doar o carte (True) sau mai multe (False)
        """
        if len(self.cards) == 0:
            screen.blit(self.placeholder_surface, self.position)
            return
        if one_held:
            start_idx = min(len(self.cards), 2)
        else:
            start_idx = min(len(self.cards), 3)
        count = 0
        for card in self.cards[-start_idx:]:
            card.draw(screen, (self.position[0] + self.offset[0] * count, self.position[1] + self.offset[1] * count))
            count += 1


class MouseHolder(CardHolder):
    def __init__(self):
        CardHolder.__init__(self, (0, 0), None)
        self.mouse_relative_position = (0, 0)
        self.last_holder = None
        self.offset = MOUSE_HOLDER_OFFSET

    def drawCards(self, screen, position=None):
        """
        Aceasta functie deseneaza cartile continute in mouse holder pe ecran. Daca nu exista carti in holder, se poate desena un placeholder (daca acesta este definit).
        Daca nu exista carti in holder, se deseneaza un placeholder (daca este disponibil).
        Desenarea se face in functie de pozitia absoluta si offset-ul fiecarei carti in holder.
        """
        position = (self.mouse_relative_position[0] + position[0], self.mouse_relative_position[1] + position[1])
        if len(self.cards) == 0:
            if self.placeholder_surface:  # if not mouse holder
                screen.blit(self.placeholder_surface, position)
            return
        for i in range(len(self.cards)):
            self.cards[i].draw(screen, (position[0] + self.offset[0] * i, position[1] + self.offset[1] * i))

    def add_card(self, card):
        self.cards.append(card)
