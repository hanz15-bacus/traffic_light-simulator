import tkinter as tk

class TrafficLightFSM:
    def __init__(self, canvas):
        self.state = "Yellow"
        self.canvas = canvas
        self.lights = {
            "Red": self.canvas.create_oval(50, 50, 150, 150, fill="gray"),
            "Yellow": self.canvas.create_oval(50, 200, 150, 300, fill="gray"),
            "Green": self.canvas.create_oval(50, 350, 150, 450, fill="gray"),
        }
        self.update_light()

    def switch_state(self):
        if self.state == "Yellow":
            self.state = "Red"
        elif self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Off"

    def update_light(self):
        self.canvas.itemconfig(self.lights["Red"], fill="gray")
        self.canvas.itemconfig(self.lights["Yellow"], fill="gray")
        self.canvas.itemconfig(self.lights["Green"], fill="gray")

        if self.state == "Red":
            self.canvas.itemconfig(self.lights["Red"], fill="red")
        elif self.state == "Yellow":
            self.canvas.itemconfig(self.lights["Yellow"], fill="yellow")
        elif self.state == "Green":
            self.canvas.itemconfig(self.lights["Green"], fill="green")

    def run(self):
        self.update_light()

        if self.state == "Yellow":
            delay = 3000
        elif self.state == "Red":
            delay = 5000
        elif self.state == "Green":
            delay = 5000
        elif self.state == "Off":
            self.show_turn_off_message()
            self.canvas.after(2000, exit)

            return

        self.canvas.after(delay, self.next_state)

    def next_state(self):
        self.switch_state()
        self.run()

    def show_turn_off_message(self):
        self.canvas.create_text(100, 250, text="Traffic light turned off", fill="black", font=("Helvetica", 16))

def main():
    root = tk.Tk()
    root.title("Traffic Light Simulation")

    canvas = tk.Canvas(root, width=200, height=500, bg="white")
    canvas.pack()

    traffic_light = TrafficLightFSM(canvas)
    traffic_light.run()

    root.mainloop()

if __name__ == "__main__":
    main()
