import tkinter as tk
import pygame
import draw_graph_page
import draw_table_page

class WelcomePage(tk.Frame):
    def __init__(self, container, ff_time=None, ff_bv=None, ff_my=None, hm_time=None, hm_bxv=None, hm_byv=None, hm_mx=None, hm_my=None):
        super().__init__(container)

        # self.assets = assets.Assets()
        self.ff_movement_y = ff_my
        self.ff_ball_velocity = ff_bv
        self.ff_time = ff_time

        self.hm_movement_x = hm_mx
        self.hm_movement_y = hm_my
        self.hm_ball_x_velocity = hm_bxv
        self.hm_ball_y_velocity = hm_byv
        self.hm_time = hm_time

        self.create_widgets()

    # 학생 로그인 버튼 클릭 시 실행
    def free_fall(self):
        # 화면 크기
        WIDTH, HEIGHT = 800, 1000

        # 가속도 (m/s^2)
        ACCELERATION = 9.8

        self.ff_time = []
        self.ff_movement_y = []
        self.ff_ball_velocity = []

        class Ball:
            def __init__(self, x, y, radius):
                self.x = x
                self.y = y
                self.radius = radius
                self.velocity = 0  # 초기 속도
                self.timer = 0  # 타이머 초기화
                self.prev_ball_pos = []  # 이전 위치 저장 리스트

            def update(self, dt):
                # 가속도를 적용하여 속도 업데이트
                self.velocity += ACCELERATION * dt
                # 이동
                self.y += self.velocity * dt

            def draw(self, screen):
                font = pygame.font.SysFont(None, 40)
                text = font.render(f"y: {self.y:.1f}", True, (0, 0, 0))
                screen.blit(text, (self.x + 20, int(self.y) - 30))

                # 현재 위치에 공 그리기
                pygame.draw.circle(screen, (255, 0, 0), (self.x, int(self.y)), self.radius)
                # 이전 위치에 공 그리기
                for pos in self.prev_ball_pos:
                    pygame.draw.circle(screen, (255, 0, 0), (pos[0], int(pos[1])), self.radius)
                    # 이전 위치에서 x 좌표에 10을 더한 곳에 y 좌표 표시
                    text = font.render(f"y: {pos[1]:.1f}", True, (0, 0, 0))
                    screen.blit(text, (pos[0] + 10, int(pos[1]) - 20))


        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("떨어지는 공")

        clock = pygame.time.Clock()
        s = 0
        ball = Ball(WIDTH // 4, 0, 20)  # 공의 초기 위치 및 크기 설정
        started = False  # 공이 시작되었는지 여부

        running = True
        while running:
            dt = clock.tick(60) / 500.0  # 초당 프레임 수로 경과된 시간을 계산 (초 단위)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 버튼을 누를 때
                    if 550 <= event.pos[0] <= 700 and 350 <= event.pos[1] <= 500:  # 시작 버튼 영역 내에 있는지 확인
                        started = True
                    elif 550 <= event.pos[0] <= 700 and 600 <= event.pos[1] <= 750:  # 종료 버튼 영역 내에 있는지 확인
                        started = False

            if started:  # START 버튼을 누르면 공이 내려오기 시작
                ball.update(dt)

                # 타이머가 1초 이상 경과했을 때 이전 위치에 공을 저장하고, 현재 위치에 공을 그립니다.
                ball.timer += dt
                if ball.timer >= 1:
                    ball.prev_ball_pos.append((ball.x, ball.y))
                    ball.timer = 0  # 타이머 초기화
                    if len(self.ff_movement_y) <= 15:
                        if not s >= 15:
                            s += 1
                        self.ff_movement_y.append(int(f'{ball.y:.0f}'))
                        self.ff_ball_velocity.append(float(f'{ball.velocity:.1f}'))
                        self.ff_time.append(s)

            screen.fill((255, 255, 255))  # 화면을 흰색으로 지우기
            ball.draw(screen)

            # 시작 버튼 그리기
            pygame.draw.rect(screen, (0, 255, 0), (550, 350, 150, 150))  # 시작 버튼 위치 및 크기
            font = pygame.font.SysFont(None, 40)
            text = font.render("START", True, (255, 255, 255))
            screen.blit(text, (585, 410))

            # 종료 버튼 그리기
            pygame.draw.rect(screen, (255, 0, 0), (550, 600, 150, 150))  # 종료 버튼 위치 및 크기
            text = font.render("STOP", True, (255, 255, 255))
            screen.blit(text, (585, 660))

            # 타이머 표시
            timer_text = font.render(f"Timer: {s} sec", True, (0, 0, 0))
            screen.blit(timer_text, (WIDTH - 300, 20))  # 화면 오른쪽 상단에 표시

            ball_y_text = font.render(f"y: {ball.y:.1f}", True, (0, 0, 0))
            screen.blit(ball_y_text, (WIDTH - 300, 80))  # 화면 오른쪽 상단에 표시

            pygame.display.flip()
            # 게임 루프 내에서 종료 조건을 확인하고, 종료되면 루프를 빠져나오도록 함
            if not running:
                break

    def horizontal_movement(self):
        # 화면 크기
        WIDTH, HEIGHT = 1400, 1000

        # 가속도 (m/s^2)
        Y_ACCELERATION = 9.8

        # 리스트 초기화
        self.hm_movement_x = []
        self.hm_movement_y = []
        self.hm_ball_x_velocity = []
        self.hm_ball_y_velocity = []
        self.hm_time = []

        class Ball:
            def __init__(self, x, y, radius):
                self.x = x
                self.y = y
                self.radius = radius
                self.x_velocity = 0 # 초기 속도
                self.y_velocity = 0
                self.timer = 0  # 타이머 초기화
                self.prev_ball_pos = []  # 이전 위치 저장 리스트

            def update(self, dt):
                # 가속도를 적용하여 속도 업데이트
                self.y_velocity += Y_ACCELERATION * dt
                # 이동
                self.y += self.y_velocity * dt
                self.x += self.x_velocity * dt

            def draw(self, screen):
                font = pygame.font.SysFont(None, 40)
                y_text = font.render(f"y: {self.y:.1f}", True, (0, 0, 0))
                screen.blit(y_text, (self.x + 20, int(self.y) - 30))

                x_text = font.render(f"x: {self.x:.1f}", True, (0, 0, 0))
                screen.blit(x_text, (self.x + 20, int(self.y) - 50))

                # 현재 위치에 공 그리기
                pygame.draw.circle(screen, (255, 0, 0), (self.x, int(self.y)), self.radius)
                # 이전 위치에 공 그리기
                for pos in self.prev_ball_pos:
                    pygame.draw.circle(screen, (255, 0, 0), (pos[0], int(pos[1])), self.radius)
                    # 이전 위치에서 x 좌표에 10을 더한 곳에 y 좌표 표시
                    y_text = font.render(f"y: {pos[1]:.1f}", True, (0, 0, 0))
                    screen.blit(y_text, (pos[0] + 10, int(pos[1]) - 20))

                    x_text = font.render(f"x: {pos[0]:.1f}", True, (0, 0, 0))
                    screen.blit(x_text, (pos[0] + 10, int(pos[1]) - 40))


        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("떨어지는 공")

        # 폰트 설정
        font = pygame.font.Font(None, 35)

        # 입력 상자 설정
        self.input_rect = pygame.Rect(1075, 200, 200, 100)
        self.input_text = 0
        self.input_active = False

        clock = pygame.time.Clock()
        s = 0
        ball = Ball( 0, 0, 20)  # 공의 초기 위치 및 크기 설정
        started = False  # 공이 시작되었는지 여부

        def text_input(event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.input_active = False
                    ball.x_velocity = int(self.input_text)
                    self.input_text = 0
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = str(self.input_text)
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text = str(self.input_text)
                    self.input_text += event.unicode

        running = True
        while running:
            dt = clock.tick(60) / 500.0  # 초당 프레임 수로 경과된 시간을 계산 (초 단위)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 버튼을 누를 때
                    if 1100 <= event.pos[0] <= 1250 and 350 <= event.pos[1] <= 500:  # 시작 버튼 영역 내에 있는지 확인
                        started = True
                    elif 1100 <= event.pos[0] <= 1250 and 600 <= event.pos[1] <= 750:  # 종료 버튼 영역 내에 있는지 확인
                        started = False


                    if self.input_rect.collidepoint(event.pos):
                        self.input_active = True
                    else:
                        self.input_active = False

                # 입력 상자에 키 입력
                if self.input_active:
                    text_input(event)

            if started:  # START 버튼을 누르면 공이 내려오기 시작
                ball.update(dt)

                # 타이머가 1초 이상 경과했을 때 이전 위치에 공을 저장하고, 현재 위치에 공을 그립니다.
                ball.timer += dt
                if ball.timer >= 1:
                    ball.prev_ball_pos.append((ball.x, ball.y))
                    ball.timer = 0  # 타이머 초기화
                    if len(self.hm_movement_y) <= 15:
                        if not s >= 15:
                            s += 1
                        self.hm_movement_x.append(int(f'{ball.x:.0f}'))
                        self.hm_movement_y.append(int(f'{ball.y:.0f}'))
                        self.hm_ball_x_velocity.append(float(f'{ball.x_velocity:.1f}'))
                        self.hm_ball_y_velocity.append(float(f'{ball.y_velocity:.1f}'))
                        self.hm_time.append(s)

            screen.fill((255, 255, 255))  # 화면을 흰색으로 지우기
            ball.draw(screen)

            # 입력 칸 버튼 그리기
            pygame.draw.rect(screen, 'black', self.input_rect, 2)
            if self.input_active:
                input_surface = font.render(str(self.input_text) + "|", True, 'black')  # 깜빡이는 커서 추가
            else:
                input_surface = font.render(str(self.input_text), True, 'black')
            screen.blit(input_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

            # 시작 버튼 그리기
            pygame.draw.rect(screen, (0, 255, 0), (1100, 350, 150, 150))  # 시작 버튼 위치 및 크기
            font = pygame.font.SysFont(None, 40)
            text = font.render("START", True, (255, 255, 255))
            screen.blit(text, (1135, 410))

            # 종료 버튼 그리기
            pygame.draw.rect(screen, (255, 0, 0), (1100, 600, 150, 150))  # 종료 버튼 위치 및 크기
            text = font.render("STOP", True, (255, 255, 255))
            screen.blit(text, (1135, 660))

            # 타이머 표시
            timer_text = font.render(f"Timer: {s} sec", True, (0, 0, 0))
            screen.blit(timer_text, (WIDTH - 300, 20))  # 화면 오른쪽 상단에 표시

            ball_x_text = font.render(f"x: {ball.x:.1f}", True, (0, 0, 0))
            screen.blit(ball_x_text, (WIDTH - 300, 50))  # 화면 오른쪽 상단에 표시

            ball_y_text = font.render(f"y: {ball.y:.1f}", True, (0, 0, 0))
            screen.blit(ball_y_text, (WIDTH - 300, 80))  # 화면 오른쪽 상단에 표시

            ball_x_velocity_text = font.render(f"Velocity: {ball.x_velocity}", True, (0, 0, 0))
            screen.blit(ball_x_velocity_text, (1100, 300))  # 화면 오른쪽 상단에 표시

            pygame.display.flip()

            # 게임 루프 내에서 종료 조건을 확인하고, 종료되면 루프를 빠져나오도록 함
            if not running:
                break

    # 표 만드는 프레임
    def forward_to_draw_table_page(self):
        self.welcome_page_fm.destroy()
        self.update()

        dg_page_frame = draw_table_page.DTPage(self, self.ff_time, self.ff_ball_velocity, self.ff_movement_y, self.hm_time, self.hm_ball_x_velocity,
                                               self.hm_ball_y_velocity, self.hm_movement_x, self.hm_movement_y)
        dg_page_frame.pack()



    # 그래프 만드는 프레임
    def forward_to_draw_graph_page(self):
        self.welcome_page_fm.destroy()
        self.update()

        dg_page_frame = draw_graph_page.DGPage(self, self.ff_time, self.ff_ball_velocity, self.ff_movement_y, self.hm_time, self.hm_ball_x_velocity,
                                               self.hm_ball_y_velocity, self.hm_movement_x, self.hm_movement_y)
        dg_page_frame.pack()



    def create_widgets(self):
        self.welcome_page_fm = tk.Frame(self, highlightbackground='black', highlightthickness=2)

        heading_lb = tk.Label(self.welcome_page_fm, text='운동 비교 시스템', bg='sky blue',
                              fg='white',
                              font=('Bold', 18))
        heading_lb.place(x=0, y=0, width=396)

        free_fall_btn = tk.Button(self.welcome_page_fm, text='자유 낙하 운동', bg='blue', fg='white',
                                      font=('Bold', 15),
                                      command=self.free_fall)
        free_fall_btn.place(x=105, y=88, width=200)

        horizontal_movement_btn = tk.Button(self.welcome_page_fm, text='수평 방향으로 던진\n 물체의 운동', bg='blue', fg='white',
                                  font=('Bold', 15),
                                  command=self.horizontal_movement
                                  )
        horizontal_movement_btn.place(x=105, y=158, width=200, height=50)

        make_table_btn = tk.Button(self.welcome_page_fm, text='표 그리기', bg='blue', fg='white',
                                   font=('Bold', 15),
                                   command=self.forward_to_draw_table_page)
        make_table_btn.place(x=105, y=238, width=200)

        make_graph_btn = tk.Button(self.welcome_page_fm, text='그래프 그리기', bg='blue', fg='white',
                                  font=('Bold', 15),
                                  command=self.forward_to_draw_graph_page)
        make_graph_btn.place(x=105, y=313, width=200)

        self.welcome_page_fm.pack(pady=30)
        self.welcome_page_fm.configure(width=400, height=420)