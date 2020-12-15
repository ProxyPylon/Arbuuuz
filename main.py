from superwires import games, color
import random



class Water_Melon(games.Sprite):
    """qweqweqwe123"""
    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = - self.dx
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = - self.dy

class Water_Melon_rand_jump(games.Sprite):
    """qweqweqwe123"""
    def update(self):
        if self.right > games.screen.width or self.left < 0:
            rand = random.random() + 0.5
            self.dx = - (self.dx * (rand + 0.1))

        if self.bottom > games.screen.height or self.top < 0:
            rand = random.random()+0.5
            self.dy = - (self.dy * (rand + 0.1))


            #################txt.hand_update(txt, self.dy)



class New_Text(games.Text):
    def hand_update(self, str_type):
        self.value = str_type



def main():
    games.init(screen_width=708, screen_height=800, fps=60)

    wall_image = games.load_image("aska2.jpg", transparent=False)
    games.screen.background = wall_image

    arbuz_img = games.load_image("арбуз_120_recoloRED.png", transparent=True)
    ar_1 = games.Sprite(image=arbuz_img, x=160, y=200, dx=4)

    #txt = games.Text(value="123qweasd", size= 80, color=(255, 30, 40), x=350, y=30)
    txt =New_Text(value="123qweasd", size=80, color=(255, 30, 40), x=350, y=30)

    ar_2 = Water_Melon_rand_jump(image=arbuz_img, x=160, y=500, dx=5, dy=3)


    games.screen.add(ar_1)
    games.screen.add(ar_2)
    games.screen.add(txt)


    games.screen.mainloop()

if __name__ == '__main__':
    main()