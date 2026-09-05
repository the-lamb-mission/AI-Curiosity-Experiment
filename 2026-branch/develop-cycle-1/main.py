import pygame

pygame.init()

screen = pygame.display.set_mode((960, 960))
pygame.display.set_caption("AI Curiosity Simulation (2026 branch)")

end_condition = False
while not end_condition:

    screen.fill("gray")
    pygame.display.flip()

    moderatorInput = input("Instruction: (Type Stop to stop)")
    end_condition = (moderatorInput == "Stop") or (moderatorInput == "stop")
