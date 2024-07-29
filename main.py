import pygame
import numpy as np
import sys
from labirentler import Maze

class Main:
    def __init__(self):
        # Pygame başlatılıyor ve ekran ayarlanıyor
        pygame.init()
        self.screen = pygame.display.set_mode((600, 540))
        pygame.display.set_caption('Labirent Q-Learn')

        # Başlangıç labirenti yükleniyor
        self.labirent_baslangic = 0
        self.labirent = Maze.maze(self.labirent_baslangic)
        if self.labirent is None:
            print("Labirent yüklenemedi")
            sys.exit()

        # Blok boyutu ve oyuncu/bananın başlangıç konumu ayarlanıyor
        self.block_size = 60
        self.player_pos = [1, 1]
        self.banana_pos = [1, 7]

        # Görseller yükleniyor
        self.player_image = pygame.image.load('images/monkey.bmp')
        self.banana_image = pygame.image.load('images/banana.bmp')

        # Q-Öğrenme parametreleri ayarlanıyor
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1
        self.q_table = np.zeros((len(self.labirent), len(self.labirent[0]), 4))

        # İzleme için değişkenler tanımlanıyor
        self.total_q_change = 0
        self.num_steps = 0
        self.sayac = 0

    def draw_maze(self):
        # Labirenti çizen fonksiyon
        for row in range(len(self.labirent)):
            for col in range(len(self.labirent[row])):
                color = (255, 255, 255) if self.labirent[row][col] == 1 else (0, 0, 0)
                pygame.draw.rect(self.screen, color,
                                 (col * self.block_size, row * self.block_size, self.block_size, self.block_size))

    def draw_monkey(self):
        # Oyuncuyu çizen fonksiyon
        self.screen.blit(self.player_image,
                         (self.player_pos[0] * self.block_size, self.player_pos[1] * self.block_size))

    def draw_banana(self):
        # Bananayı çizen fonksiyon
        self.screen.blit(self.banana_image,
                         (self.banana_pos[0] * self.block_size, self.banana_pos[1] * self.block_size))

    def move_player(self, action):
        # Oyuncuyu hareket ettiren fonksiyon
        directions = ['up', 'down', 'left', 'right']
        direction_vectors = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}
        dx, dy = direction_vectors[directions[action]]
        new_pos = [self.player_pos[0] + dx, self.player_pos[1] + dy]

        # Yeni pozisyon geçerli mi kontrol ediliyor
        if (0 <= new_pos[0] < len(self.labirent[0])) and (0 <= new_pos[1] < len(self.labirent)) and (self.labirent[new_pos[1]][new_pos[0]] == 0):
            reward = -0.1
            if new_pos == self.banana_pos:
                reward = 1
                # Q tablosunu güncellemeden önce yeni durumu ve ödülü kullanın
                current_state = tuple(self.player_pos)
                next_state = tuple(new_pos)
                action_index = directions.index(directions[action])

                old_q_value = self.q_table[current_state[1]][current_state[0]][action_index]
                self.update_q_table(current_state, action_index, reward, next_state)
                new_q_value = self.q_table[current_state[1]][current_state[0]][action_index]

                self.total_q_change += abs(new_q_value - old_q_value)
                self.num_steps += 1

                # Labirenti ve oyuncu konumunu yeniden yükle
                self.labirent = Maze.maze(self.labirent_baslangic)
                self.player_pos = [1, 1]
                self.sayac += 1
            else:
                current_state = tuple(self.player_pos)
                next_state = tuple(new_pos)
                action_index = directions.index(directions[action])

                old_q_value = self.q_table[current_state[1]][current_state[0]][action_index]
                self.update_q_table(current_state, action_index, reward, next_state)
                new_q_value = self.q_table[current_state[1]][current_state[0]][action_index]

                self.total_q_change += abs(new_q_value - old_q_value)
                self.num_steps += 1

                self.player_pos = new_pos

    def update_q_table(self, state, action, reward, next_state):
        # Q tablosunu güncelleyen fonksiyon
        best_next_action = np.argmax(self.q_table[next_state[1]][next_state[0]])
        td_target = reward + self.gamma * self.q_table[next_state[1]][next_state[0]][best_next_action]
        td_error = td_target - self.q_table[state[1]][state[0]][action]
        self.q_table[state[1]][state[0]][action] += self.alpha * td_error

    def choose_action(self, state):
        # Epsilon-greedy politika ile hareket seçimi
        if np.random.rand() < self.epsilon:
            return np.random.randint(4)
        else:
            return np.argmax(self.q_table[state[1]][state[0]])

    def run(self):
        # Oyun döngüsü
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            state = tuple(self.player_pos)
            action = self.choose_action(state)

            self.move_player(action)

            self.screen.fill((0, 0, 0))
            self.draw_maze()
            self.draw_monkey()
            self.draw_banana()

            if self.num_steps > 0:
                avg_q_change = self.total_q_change / self.num_steps
                font = pygame.font.Font(None, 36)
                text = font.render(f'Ortalama Q-Değeri Değişikliği: {avg_q_change:.4f}       Ödül: {self.sayac}', True, (0, 0, 0))
                self.screen.blit(text, (10, 10))

            pygame.display.flip()

if __name__ == '__main__':
    Main().run()
