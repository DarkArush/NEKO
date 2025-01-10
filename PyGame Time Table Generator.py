import sys
import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timetable Generator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

# Dictionary to store the timetable
timetable = {}
feedbacks = []

# Function to render text
def render_text(text, x, y, color=BLACK, font=font):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main menu buttons
def main_menu_buttons():
    buttons = [
        {"label": "Generate Timetable", "rect": pygame.Rect(300, 150, 200, 50)},
        {"label": "Show Timetable", "rect": pygame.Rect(300, 220, 200, 50)},
        {"label": "Update Timetable", "rect": pygame.Rect(300, 290, 200, 50)},
        {"label": "Feedback System", "rect": pygame.Rect(300, 360, 200, 50)},
        {"label": "Exit", "rect": pygame.Rect(300, 430, 200, 50)}
    ]
    return buttons

def draw_buttons(buttons):
    for button in buttons:
        pygame.draw.rect(screen, GRAY, button["rect"])
        pygame.draw.rect(screen, BLACK, button["rect"], 2)
        render_text(button["label"], button["rect"].x + 10, button["rect"].y + 10, font=small_font)

def generate_timetable():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    timetable.clear()
    running = True
    while running:
        screen.fill(WHITE)
        render_text("Generate Timetable", 300, 50, BLUE)

        for i, day in enumerate(days):
            render_text(f"{day}: Click to add schedule", 50, 100 + i * 40, BLACK)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, day in enumerate(days):
                    if 50 <= event.pos[0] <= 750 and 100 + i * 40 <= event.pos[1] <= 140 + i * 40:
                        add_schedule(day)

def add_schedule(day):
    running = True
    activities = []
    input_box = pygame.Rect(50, 500, 700, 40)
    user_text = ""

    while running:
        screen.fill(WHITE)
        render_text(f"Add Schedule for {day}", 300, 50, BLUE)
        render_text("Type activity and press ENTER to add. Press ESC to save and go back.", 50, 450, BLACK)

        for i, activity in enumerate(activities):
            render_text(f"{i + 1}. {activity}", 50, 100 + i * 30, BLACK)

        pygame.draw.rect(screen, GRAY, input_box)
        pygame.draw.rect(screen, BLACK, input_box, 2)
        render_text(user_text, input_box.x + 10, input_box.y + 10, BLACK)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_text.strip():
                        activities.append(user_text.strip())
                        user_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    timetable[day] = activities
                    running = False
                else:
                    user_text += event.unicode

def update_timetable():
    days = list(timetable.keys())
    if not days:
        return

    running = True
    while running:
        screen.fill(WHITE)
        render_text("Update Timetable", 300, 50, BLUE)

        for i, day in enumerate(days):
            render_text(f"{i + 1}. {day}: Click to update schedule", 50, 100 + i * 40, BLACK)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, day in enumerate(days):
                    if 50 <= event.pos[0] <= 750 and 100 + i * 40 <= event.pos[1] <= 140 + i * 40:
                        edit_schedule(day)

def edit_schedule(day):
    activities = timetable.get(day, [])
    running = True
    input_box = pygame.Rect(50, 500, 700, 40)
    user_text = ""

    while running:
        screen.fill(WHITE)
        render_text(f"Edit Schedule for {day}", 300, 50, BLUE)
        render_text("Type activity and press ENTER to add/update. Press ESC to save and go back.", 50, 450, BLACK)

        for i, activity in enumerate(activities):
            render_text(f"{i + 1}. {activity}", 50, 100 + i * 30, BLACK)

        pygame.draw.rect(screen, GRAY, input_box)
        pygame.draw.rect(screen, BLACK, input_box, 2)
        render_text(user_text, input_box.x + 10, input_box.y + 10, BLACK)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_text.strip():
                        activities.append(user_text.strip())
                        user_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    timetable[day] = activities
                    running = False
                else:
                    user_text += event.unicode

def feedback_system():
    running = True
    input_box = pygame.Rect(50, 500, 700, 40)
    user_text = ""

    while running:
        screen.fill(WHITE)
        render_text("Feedback System", 300, 50, BLUE)
        render_text("Type your feedback and press ENTER to submit. Press ESC to go back.", 50, 450, BLACK)

        for i, feedback in enumerate(feedbacks):
            render_text(f"{i + 1}. {feedback}", 50, 100 + i * 30, BLACK)

        pygame.draw.rect(screen, GRAY, input_box)
        pygame.draw.rect(screen, BLACK, input_box, 2)
        render_text(user_text, input_box.x + 10, input_box.y + 10, BLACK)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_text.strip():
                        feedbacks.append(user_text.strip())
                        user_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    user_text += event.unicode

def show_timetable():
    running = True
    while running:
        screen.fill(WHITE)
        render_text("Timetable", 300, 50, BLUE)
        y_offset = 100

        if not timetable:
            render_text("No timetable available.", 300, y_offset, BLACK)
        else:
            for day, activities in timetable.items():
                render_text(f"{day}: {', '.join(activities)}", 50, y_offset, BLACK)
                y_offset += 40

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# Main menu loop
def main_menu():
    running = True
    buttons = main_menu_buttons()

    while running:
        screen.fill(WHITE)
        render_text("Timetable Generator", 300, 50, BLUE)
        draw_buttons(buttons)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        if button["label"] == "Generate Timetable":
                            generate_timetable()
                        elif button["label"] == "Show Timetable":
                            show_timetable()
                        elif button["label"] == "Update Timetable":
                            update_timetable()
                        elif button["label"] == "Feedback System":
                            feedback_system()
                        elif button["label"] == "Exit":
                            running = False

if __name__ == "__main__":
    main_menu()