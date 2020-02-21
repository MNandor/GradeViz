import data
import pygame

juds = {
"BC":(635,275),
"MS":(435,245),
"CV":(560,340),
"BN":(400,150),
"CJ":(350,205),
"SJ":(280,160),
"BV":(490,365),
"TM":(120,350),
"SM":(265,90),
"B":(570,540),
"MM":(375,95),
"BH":(185,190),
"AB":(330,305),
"HR":(520,255),
"HD":(270,360),
"AR":(160,275),
"SB":(395,350),
}

running = True

width = 918
height = 642
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
bg = pygame.image.load("newMap.png")
marker = pygame.image.load("marker.png")
selmark = pygame.image.load("select.png")

select = []

def toggle(pos):
	print(pos)
	global select
	for p in juds:
		if abs(juds[p][0]-pos[0]) < 7 and abs(juds[p][1]-pos[1]) < 7:
			print(p)
			if p in select:
				select.remove(p)
			else:
				select += [p]
			break

def openJud(pos):
	for p in juds:
		if abs(juds[p][0]-pos[0]) < 7 and abs(juds[p][1]-pos[1]) < 7:
			data.judViz(p)
			break
	

def frameEnd():
	global running
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			running = False
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			if event.button == 1: #left
				toggle(pos)
			elif event.button == 3: #right
				openJud(pos)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if len(select) > 0:
					data.viz(select)
			if event.key == pygame.K_a:
				for p in juds:
					toggle(juds[p])
			if event.key == pygame.K_1:
				data.hideUnhide(1)
			if event.key == pygame.K_2:
				data.hideUnhide(2)
			if event.key == pygame.K_3:
				data.hideUnhide(3)
			if event.key == pygame.K_4:
				data.hideUnhide(0)
					


while running:
	screen.blit(bg, (0,0))
	for p in juds:
		g = [x-6 for x in juds[p]]
		if p in select:
			screen.blit(selmark, g)
		else:
			screen.blit(marker, g)

	frameEnd()