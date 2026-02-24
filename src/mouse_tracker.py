import pygame

class MouseTracker:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        print('Left mouse button clicked at:', event.pos)
                    elif event.button == 3:  # Right click
                        print('Right mouse button clicked at:', event.pos)

        pygame.quit()

if __name__ == '__main__':
    tracker = MouseTracker()
    tracker.run()