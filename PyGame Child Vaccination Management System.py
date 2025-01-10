import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Child Vaccination Management System")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

# Data storage
children = {}

# Helper Functions
def render_text(text, x, y, color=BLACK, font=font):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def generate_child_id():
    return str(len(children) + 1).zfill(5)

def main_menu_buttons():
    buttons = [
        {"label": "Add Child Entry", "rect": pygame.Rect(300, 150, 200, 50)},
        {"label": "Delete Child Entry", "rect": pygame.Rect(300, 220, 200, 50)},
        {"label": "Show Child Entry", "rect": pygame.Rect(300, 290, 200, 50)},
        {"label": "Update Child Entry", "rect": pygame.Rect(300, 360, 200, 50)},
        {"label": "Exit", "rect": pygame.Rect(300, 430, 200, 50)}
    ]
    return buttons

def draw_buttons(buttons):
    for button in buttons:
        pygame.draw.rect(screen, GRAY, button["rect"])
        pygame.draw.rect(screen, BLACK, button["rect"], 2)
        render_text(button["label"], button["rect"].x + 10, button["rect"].y + 10, font=small_font)

# Features

def add_child_entry():
    inputs = ["Child's Name", "Date of Birth (DD/MM/YYYY)", "Gender", "Parent's Name", "Contact No"]
    data = {}
    input_box = pygame.Rect(50, 500, 700, 40)
    user_text = ""
    current_input = 0

    running = True
    while running:
        screen.fill(WHITE)
        render_text("Add Child Entry", 300, 50, BLUE)
        render_text(f"Enter {inputs[current_input]}:", 50, 450, BLACK)

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
                        data[inputs[current_input]] = user_text.strip()
                        user_text = ""
                        current_input += 1

                        if current_input >= len(inputs):
                            child_id = generate_child_id()
                            children[child_id] = data
                            screen.fill(WHITE)
                            render_text(f"Child ID: {child_id} added successfully!", 50, 100, BLUE)
                            pygame.display.flip()
                            pygame.time.wait(3000)
                            running = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    user_text += event.unicode

def delete_child_entry():
    input_box = pygame.Rect(50, 500, 700, 40)
    user_text = ""
    running = True

    while running:
        screen.fill(WHITE)
        render_text("Delete Child Entry", 300, 50, BLUE)
        render_text("Enter Child ID to delete:", 50, 450, BLACK)

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
                    if user_text.strip() in children:
                        del children[user_text.strip()]
                    user_text = ""
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    user_text += event.unicode

def show_child_entry():
    input_box = pygame.Rect(50, 500, 700, 40)
    user_text = ""
    running = True

    while running:
        screen.fill(WHITE)
        render_text("Show Child Entry", 300, 50, BLUE)
        render_text("Enter Child ID to view details:", 50, 450, BLACK)

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
                    if user_text.strip() in children:
                        details = children[user_text.strip()]
                        screen.fill(WHITE)
                        render_text(f"Details for Child ID: {user_text.strip()}", 50, 50, BLUE)
                        y = 100
                        for key, value in details.items():
                            render_text(f"{key}: {value}", 50, y, BLACK)
                            y += 40
                        render_text(f"Child ID: {user_text.strip()}", 50, y, BLACK)
                        pygame.display.flip()
                        pygame.time.wait(5000)
                    user_text = ""
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    user_text += event.unicode

def update_child_entry():
    input_box = pygame.Rect(50, 500, 700, 40)
    user_text = ""
    running = True
    selected_id = None

    while running:
        screen.fill(WHITE)
        if not selected_id:
            render_text("Update Child Entry", 300, 50, BLUE)
            render_text("Enter Child ID to update:", 50, 450, BLACK)
        else:
            render_text(f"Update Entry for Child ID: {selected_id}", 300, 50, BLUE)
            render_text("Enter key=value to update (e.g., Name=John):", 50, 450, BLACK)

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
                    if not selected_id:
                        if user_text.strip() in children:
                            selected_id = user_text.strip()
                        user_text = ""
                    else:
                        if "=" in user_text:
                            key, value = user_text.split("=", 1)
                            if key in children[selected_id]:
                                children[selected_id][key] = value
                        user_text = ""
                        running = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    user_text += event.unicode

# Main Menu
def main_menu():
    running = True
    buttons = main_menu_buttons()

    while running:
        screen.fill(WHITE)
        render_text("Child Vaccination Management System", 200, 50, BLUE)
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
                        if button["label"] == "Add Child Entry":
                            add_child_entry()
                        elif button["label"] == "Delete Child Entry":
                            delete_child_entry()
                        elif button["label"] == "Show Child Entry":
                            show_child_entry()
                        elif button["label"] == "Update Child Entry":
                            update_child_entry()
                        elif button["label"] == "Exit":
                            running = False

if __name__ == "__main__":
    main_menu()