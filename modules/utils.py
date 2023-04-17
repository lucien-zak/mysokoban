import pygame


class Utils:

    def detectCollideBoxes(boxes, player, event):
        if player.rect.collidelist(boxes) != -1:
            boxes[player.rect.collidelist(boxes)].move(event)
            
                    
                        
                    
