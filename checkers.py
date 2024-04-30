import pygame,os
pygame.init()
path = os.path.dirname(os.path.realpath(__file__))
ts = 80
mx = -1
my = -1
oy = ts/2
def floor(num):
  return round(num//1)
screen = pygame.display.set_mode((floor(ts*8),floor(ts*8.5)))
pygame.display.set_caption("Checkers")
font = pygame.font.Font((str(path)+'/assets/fonts/font.ttf'),floor(oy))
text = font.render("T u r n",True,(255,255,255))
t_rect = text.get_rect(center=(ts*4,floor(oy/2)))
wins = font.render("W I N N E R",True,(255,255,255))
w_rect = wins.get_rect(center=(ts*4,floor(oy/2)))
def draw_checkers():
  for i in range(8):
    for j in range(8):
      if (i+j)%2 == 1:
        pygame.draw.rect(screen,(0,0,0),((j*ts),(i*ts)+oy,ts,ts))
      else:
        pygame.draw.rect(screen,(255,255,255),((j*ts),(i*ts)+oy,ts,ts))
def checkib(x,y):
  if x > 7 or x < 0 or y > 7 or y < 0:
    return False
  return True
set_board = [[0,1,0,1,0,1,0,1],
             [1,0,1,0,1,0,1,0],
             [0,1,0,1,0,1,0,1],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [2,0,2,0,2,0,2,0],
             [0,2,0,2,0,2,0,2],
             [2,0,2,0,2,0,2,0],]
blank_board = [[0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],]
board = set_board.copy()
#board = blank_board.copy()
all_moves = []
turn = 1
ded = 0
checker_a = (80,80,80)
checker_b = (200,0,0)
checker_ka = (40,40,40)
checker_kb = (150,0,0)
beven = (161,97,23)
bodd = (212,160,87)
def gen_high(r,g,b,a):
  highlight = pygame.Surface((ts,ts),pygame.SRCALPHA)
  highlight.fill((r,g,b,a))
  return highlight
r_high = gen_high(255,0,0,128)
y_high = gen_high(255,255,0,128)
g_high = gen_high(0,255,0,128)
class AnyNum:
  def __eq__(self,other):
    return True
Any = AnyNum()
def get_moves(x,y,op,curr_out=[],fk=False,lmj=False,addr=False):
  def check_move(x,y,dx,dy,extra=''):
    try:
      if board[y+dy][x+dx]%2 == side and board[y+dy][x+dx] != 0:
        return False
      if x+dx < 0 or x+dx > 7 or y+dy < 0 or y+dy > 7:
        return False
      if board[y+dy][x+dx] == 0:
        if extra=='cj':
          return False
        elif extra=='pos':
          return [[x+dx,y+dy]]
        else:
          return True
      else:
        if board[y+dy+dy][x+dx+dx] == 0:
          if extra=='cj':
            return True
          elif extra=='pos':
            return [[x+dx+dx,y+dy+dy]]
          else:
            return True
        else:
          return False
    except:
      return False
  def listadd(a,b):
    for c in b:
      if not [c[0],c[1],Any,Any] in a:
        if c[0] >= 0 and c[0] <= 7 and c[1] >= 0 and c[1] <= 8:
          a.append(c)
    return(a)
  def chkkng(y,dy,op):
    try:
      if op == 1:
        if y+dy == 7:
          return True
      elif op == 2:
        if y+dy == 0:
          return True
      elif op>2:
        return True
      return False
    except:
      return False
  out = curr_out
  out = listadd(out,[[x,y,[],False]])
  if fk and (not op>2):
    if op == 1 and y == 7:
      op = 3
    elif op == 2 and y == 0:
      op = 4
  character = op
  side = character%2
  if character != 2:
    if check_move(x,y,-1,1,side):
      if not lmj and not check_move(x,y,-1,1,'cj'):
        out = listadd(out,[[x-1,y+1,[],chkkng(y,1,op)]])
      if check_move(x,y,-1,1,'cj') and (not [x-2,y+2,Any,Any] in out):
        a = out.index([x,y,Any,Any])
        a = out[a][2]
        out = listadd(out,[[x-2,y+2,a+[[x-1,y+1]],chkkng(y,2,op)]])
        a = get_moves(x-2,y+2,op,out,True,True)
        out = listadd(out,a)
    if check_move(x,y,1,1):
      if not lmj and not check_move(x,y,1,1,'cj'):
        out = listadd(out,[[x+1,y+1,[],chkkng(y,1,op)]])
      if check_move(x,y,1,1,'cj') and (not [x+2,y+2,Any,Any] in out):
        a = out.index([x,y,Any,Any])
        a = out[a][2]
        out = listadd(out,[[x+2,y+2,a+[[x+1,y+1]],chkkng(y,2,op)]])
        a = get_moves(x+2,y+2,op,out,True,True)
        out = listadd(out,a)
  if character != 1:
    if check_move(x,y,-1,-1):
      if not lmj and not check_move(x,y,-1,-1,'cj'):
        out = listadd(out,[[x-1,y-1,[],chkkng(y,-1,op)]])
      if check_move(x,y,-1,-1,'cj') and (not [x-2,y-2,Any,Any] in out):
        a = out.index([x,y,Any,Any])
        a = out[a][2]
        out = listadd(out,[[x-2,y-2,a+[[x-1,y-1]],chkkng(y,-2,op)]])
        a = get_moves(x-2,y-2,op,out,True,True)
        out = listadd(out,a)
    if check_move(x,y,1,-1):
      if not lmj and not check_move(x,y,1,-1,'cj'):
        out = listadd(out,[[x+1,y-1,[],chkkng(y,-1,op)]])
      if check_move(x,y,1,-1,'cj') and (not [x+2,y-2,Any,Any] in out):
        a = out.index([x,y,Any,Any])
        a = out[a][2]
        out = listadd(out,[[x+2,y-2,a+[[x+1,y-1]],chkkng(y,-2,op)]])
        a = get_moves(x+2,y-2,op,out,True,True)
        out = listadd(out,a)
  return out
def draw_checker(id,x,y,size=ts):
  pos = floor(x*ts+(ts/2)),floor((y*ts+(ts/2))+oy)
  if id%2 == 1:
    pygame.draw.circle(screen,checker_a,pos,floor(size/2.1))
  elif id%2 == 0 and (not id == 0):
    pygame.draw.circle(screen,checker_b,pos,floor(size/2.1))
  if id == 3:
    pygame.draw.circle(screen,checker_ka,pos,floor(size/3))
  elif id == 4:
    pygame.draw.circle(screen,checker_kb,pos,floor(size/3))
def boardcount(num):
  cnt = 0
  for xrow in board:
    cnt += xrow.count(num)
  return cnt
def draw_screen(moves=True):
  global all_moves
  if ded > 0:
    if ded % 2 == 1:
      screen.fill(checker_a)
    else:
      screen.fill(checker_b)
    screen.blit(wins,w_rect)
    draw_checkers()
    draw_checker(ded,3.5,3.5,ts*8)
    pygame.display.update()
    return
  if turn == 1:
    screen.fill(checker_a)
  else:
    screen.fill(checker_b)
  screen.blit(text,t_rect)
  draw_checkers()
  for i in range(8):
    for j in range(8):
      k = board[i][j]
      draw_checker(k,j,i)
  if board[my][mx] != 0 and moves and (turn == (board[my][mx]%2)) and checkib(mx,my):
    screen.blit(y_high,(mx*ts,my*ts+oy))
    all_moves = get_moves(mx,my,board[my][mx],[])
    for move in all_moves[1:]:
      if len(move[2]) == 0:
        screen.blit(g_high,(move[0]*ts,move[1]*ts+oy))
      else:
        screen.blit(r_high,(move[0]*ts,move[1]*ts+oy))
  pygame.display.update()
draw_screen(True)
while True:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      mpos = pygame.mouse.get_pos()
      mx,my = floor(mpos[0]/ts), floor((mpos[1]-oy)/ts)
      if [mx,my,Any,Any] in all_moves[1:]:
        a = all_moves.index([mx,my,Any,Any])
        b = all_moves[a][3]
        if b==True and board[all_moves[0][1]][all_moves[0][0]]<3:
          board[my][mx] = board[all_moves[0][1]][all_moves[0][0]]+2
        else:
          board[my][mx] = board[all_moves[0][1]][all_moves[0][0]]
        board[all_moves[0][1]][all_moves[0][0]] = 0
        b = all_moves[a][2]
        for i in b:
          board[i[1]][i[0]] = 0
        all_moves = []
        turn = 1-turn
        if boardcount(1)+boardcount(3) == 0:
          ded = 4
        elif boardcount(2)+boardcount(4) == 0:
          ded = 3
        draw_screen(False)
      else:
        draw_screen()
    if event.type == pygame.QUIT:
      exit()
