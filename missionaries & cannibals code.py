### Your Code ###
boat_side= 'right'
missionaries_on_right=3
cannibals_on_right=3
missionaries_on_left=0
cannibals_on_left=0

print("💂"*missionaries_on_left,"👹"*cannibals_on_left,'|🌊🌊🌊🌊🌊🚢|','💂'*missionaries_on_right, '👹'*cannibals_on_right)
while True:
    missionaries=int(input("💂 on 🚢"))
    cannibals=int(input("👹 on 🚢 = "))

    if (missionaries+cannibals) <=2 and   (missionaries+cannibals)>=1 :
      print('ok')
    else:
      print("invalid move 1")
      continue

    if boat_side =='right':
      # print('boat is on right side')

      # if missionaries>missionaries_on_right or cannibals>cannibals_on_right:
      #   print("invalid move 2")
      #   continue
      # else:
      #   print("valid move")


      missionaries_on_right=missionaries_on_right-missionaries
      cannibals_on_right=cannibals_on_right-cannibals
      missionaries_on_left=missionaries_on_left+missionaries
      cannibals_on_left=cannibals_on_left+cannibals
      boat_side='left'
      print("💂"*missionaries_on_left,"👹"*cannibals_on_left,'|🚢🌊🌊🌊🌊🌊|','💂'*missionaries_on_right,'👹'*cannibals_on_right)


    elif boat_side=='left':
      # print('boat is on left')

      # if missionaries>missionaries_on_right or cannibals>cannibals_on_right:
      #   print("invalid move 2")
      #   continue

      missionaries_on_left=missionaries_on_left-missionaries
      cannibals_on_left=cannibals_on_left-cannibals
      missionaries_on_right=missionaries_on_right+missionaries
      cannibals_on_right=cannibals_on_right+cannibals
      boat_side = 'right'

      print("💂"*missionaries_on_left,"👹"*cannibals_on_left,'|🌊🌊🌊🌊🌊🚢|','💂'*missionaries_on_right,"👹"*cannibals_on_right)

    if missionaries_on_right<cannibals_on_right and missionaries_on_right>0:
      print('YOU LOSE')
      break
    elif missionaries_on_left<cannibals_on_left and missionaries_on_left>0:
      print('YOU LOSE')
      break
    elif missionaries_on_left==3 and cannibals_on_left==3:
      print('YOU WIN')
      break


