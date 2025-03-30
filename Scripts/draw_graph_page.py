import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import e_welcome

class DGPage(tk.Frame):
    def __init__(self, container, ff_time, ff_bv, ff_my, hm_time, hm_bxv, hm_byv, hm_mx, hm_my):
        super().__init__(container)

        self.ff_time = ff_time
        self.ff_ball_velocity = ff_bv
        self.ff_movement_y = ff_my

        self.hm_time = hm_time
        self.hm_movement_x = hm_mx
        self.hm_movement_y = hm_my
        self.hm_ball_x_velocity = hm_bxv
        self.hm_ball_y_velocity = hm_byv

        self.create_widgets()

    def ff_draw(self):
        plt.rc('font', family='Malgun Gothic')
        data = {'시간':self.ff_time, '속도':self.ff_ball_velocity, '거리':self.ff_movement_y}
        df = pd.DataFrame(data)
        columns = df.columns
        x = df[columns[0]]
        y1 = df[columns[1]]
        y2 = df[columns[2]]

        fig, ax = plt.subplots(1, 2, figsize=(14, 8))
        fig.subplots_adjust(wspace=0.5)
        ax[0].plot(x, y1)
        ax[0].set_xlabel(columns[0], fontsize=12)
        ax[0].set_ylabel(columns[1], fontsize=12)
        ax[0].grid()

        ax[1].plot(x, y2, color='orange')
        ax[1].set_xlabel(columns[0], fontsize=12)
        ax[1].set_ylabel(columns[2], fontsize=12)
        ax[1].grid()

        plt.suptitle('자유 낙하 운동', fontsize=30)
        plt.show()

    def hm_draw(self):
        plt.rc('font', family='Malgun Gothic')
        data = {'시간': self.hm_time, '수직 방향 속도': self.hm_ball_y_velocity, '수직 방향 거리': self.hm_movement_y,
                 '수평 방향 속도': self.hm_ball_x_velocity,
                 '수평 방향 거리': self.hm_movement_x}

        df = pd.DataFrame(data)

        columns = df.columns

        x = df[columns[0]]
        y1 = df[columns[1]]
        y2 = df[columns[2]]
        y3 = df[columns[3]]
        y4 = df[columns[4]]

        fig, ax = plt.subplots(2, 2, figsize=(16, 10))
        fig.subplots_adjust(wspace=0.5, hspace=0.5)

        # 각각의 서브플롯에 데이터 플롯
        ax[0, 0].plot(x, y1)
        ax[0, 0].set_xlabel(columns[0], fontsize=12)
        ax[0, 0].set_ylabel('속도', fontsize=12)
        ax[0, 0].grid()
        ax[0, 0].text(1.25, 1.05, '연직 방향', horizontalalignment='center', verticalalignment='center',
                      transform=ax[0, 0].transAxes, fontsize=20)

        ax[0, 1].plot(x, y2, color='orange')
        ax[0, 1].set_xlabel(columns[0], fontsize=12)
        ax[0, 1].set_ylabel('거리', fontsize=12)
        ax[0, 1].grid()

        ax[1, 0].plot(x, y3, color='green')
        ax[1, 0].set_xlabel(columns[0], fontsize=12)
        ax[1, 0].set_ylabel('속도', fontsize=12)
        ax[1, 0].grid()
        ax[1, 0].text(1.25, -0.4, '수평 방향', horizontalalignment='center', verticalalignment='center',
                      transform=ax[0, 0].transAxes, fontsize=20)

        ax[1, 1].plot(x, y4, color='red')
        ax[1, 1].set_xlabel(columns[0], fontsize=12)
        ax[1, 1].set_ylabel('거리', fontsize=12)
        ax[1, 1].grid()

        plt.suptitle('  수평 방향으로 던진 물체의 운동', fontsize=30)
        plt.show()

    def back_to_e_welcome_page(self):
        self.draw_graph_page_fm.destroy()
        self.update()

        e_welcome_page = e_welcome.WelcomePage(self, self.ff_time, self.ff_ball_velocity, self.ff_movement_y, self.hm_time, self.hm_ball_x_velocity,
                                               self.hm_ball_y_velocity, self.hm_movement_x, self.hm_movement_y)
        e_welcome_page.pack()

    def create_widgets(self):
        self.draw_graph_page_fm = tk.Frame(self, highlightbackground='black', highlightthickness=2)

        heading_lb = tk.Label(self.draw_graph_page_fm, text='그래프 그리기', bg='sky blue',
                              fg='white',
                              font=('Bold', 18))
        heading_lb.place(x=0, y=0, width=396)

        free_fall_btn = tk.Button(self.draw_graph_page_fm, text='자유 낙하 운동', bg='blue', fg='white',
                                  font=('Bold', 15),
                                  command=self.ff_draw)
        free_fall_btn.place(x=105, y=153, width=200)

        back_btn = tk.Button(self.draw_graph_page_fm, text='back', fg='black',
                             font=('Bold', 15, 'bold'), bd=0,
                             command=self.back_to_e_welcome_page)
        back_btn.place(x=0, y=30, width=75)

        vertical_movement_btn = tk.Button(self.draw_graph_page_fm, text='수평 방향으로 던진\n 물체의 운동', bg='blue', fg='white',
                                          font=('Bold', 15),
                                          command=self.hm_draw
                                          )
        vertical_movement_btn.place(x=105, y=243, width=200, height=50)

        self.draw_graph_page_fm.pack(pady=30)
        self.draw_graph_page_fm.configure(width=400, height=420)