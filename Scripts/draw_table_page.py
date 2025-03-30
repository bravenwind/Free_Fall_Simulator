import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import e_welcome

class DTPage(tk.Frame):
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
        plt.rcParams['font.family'] = 'Malgun Gothic'
        fig, ax = plt.subplots(1, 1, figsize=(8, 14))
        data = {"속도": self.ff_ball_velocity, "연직 방향 거리": self.ff_movement_y}
        df = pd.DataFrame(data)


        ax.axis("tight")
        ax.axis("off")
        ax.set_title('자유 낙하 운동')

        table = ax.table(
            cellText=df.values,
            colLabels=df.columns,
            rowLabels=self.ff_time,
            loc="center",
        )

        table.set_fontsize(20)
        table.scale(1, 4)


        plt.title('자유 낙하 운동')
        plt.show()

    def hm_draw(self):
        plt.rcParams['font.family'] = 'Malgun Gothic'
        fig, ax = plt.subplots(1, 1, figsize=(8, 14))
        data = {"연직 방향 속도": self.hm_ball_y_velocity, "연직 방향 거리": self.hm_movement_y,
                "수평 방향 속도": self.hm_ball_x_velocity, "수평 방향 거리":self.hm_movement_x}
        df = pd.DataFrame(data)


        ax.axis("tight")
        ax.axis("off")
        ax.set_title('수평 방향으로 던진 물체의 운동')

        table = ax.table(
            cellText=df.values,
            colLabels=df.columns,
            rowLabels=self.hm_time,
            loc="center",
        )

        table.set_fontsize(20)
        table.scale(1, 4)

        plt.show()

    def back_to_e_welcome_page(self):
        self.draw_table_page_fm.destroy()
        self.update()

        e_welcome_page = e_welcome.WelcomePage(self, self.ff_time, self.ff_ball_velocity, self.ff_movement_y, self.hm_time, self.hm_ball_x_velocity,
                                               self.hm_ball_y_velocity, self.hm_movement_x, self.hm_movement_y)
        e_welcome_page.pack()


    def create_widgets(self):
        self.draw_table_page_fm = tk.Frame(self, highlightbackground='black', highlightthickness=2)

        heading_lb = tk.Label(self.draw_table_page_fm, text='표 그리기', bg='sky blue',
                              fg='white',
                              font=('Bold', 18))
        heading_lb.place(x=0, y=0, width=396)

        free_fall_btn = tk.Button(self.draw_table_page_fm, text='자유 낙하 운동', bg='blue', fg='white',
                                  font=('Bold', 15),
                                  command=self.ff_draw)
        free_fall_btn.place(x=105, y=153, width=200)

        back_btn = tk.Button(self.draw_table_page_fm, text='back', fg='black',
                                  font=('Bold', 15, 'bold'), bd=0,
                                  command=self.back_to_e_welcome_page)
        back_btn.place(x=0, y=30, width=75)

        vertical_movement_btn = tk.Button(self.draw_table_page_fm, text='수평 방향으로 던진\n 물체의 운동', bg='blue', fg='white',
                                          font=('Bold', 15),
                                          command=self.hm_draw
                                          )
        vertical_movement_btn.place(x=105, y=243, width=200, height=50)

        self.draw_table_page_fm.pack(pady=30)
        self.draw_table_page_fm.configure(width=400, height=420)