import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)    
    kk_imgs = [kk_img]
    num = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]
    for i in num:
         kk_imgs.append(pg.transform.rotozoom(kk_img, i , 1.0))

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -(tmr % 3200)
        
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [1600+x, 0])
        screen.blit(bg_img, [x+3200, 0])

        screen.blit(kk_imgs[int((tmr%(6*len(num)))/6)], [300, 200])

        pg.display.update()
        tmr += 1        
        clock.tick(300)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()