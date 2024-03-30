class Ball:
    def __init__(self,direction = "up",color="white",size=1, height=100.0,velocity=30.0):
        self.direction = direction
        self.color = color
        self.size = size
        self.height = height
        self.velocity = velocity

    def __str__(self):
        description = "Direction = " + self.direction
        description = description + "\nColor = " + self.color
        description = description + "\nSize = " + str(self.size)
        description = description + "\nVelocity = " + str(self.velocity)
        description = description + "\nHeight = " + str(self.height)
        return description
    
    def inflate(self):
        self.size = self.size * 2
        
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"
            self.velocity = -self.velocity

    def pass_time(self):
        gravity = -9.8
        self.height = self.height + self.velocity * 1
        self.velocity = self.velocity + gravity
        if self.velocity <0:
            self.direction = "down"
        if self.height <=0:
            self.height = -self.height
            self.bounce()

            
