import pygame


class Utils:

    def detectCollideBoxes(boxes, player, event, walls):
        if player.rect.collidelist(boxes) != -1:
            boxes[player.rect.collidelist(boxes)].move(event)
        if player.rect.collidelist(walls) != -1:
            player.moveBack()
        
            
                    
                        
                    
