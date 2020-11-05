    #     self.color = Sequential(MaxPool2d(2, 2, padding=0))

    #     self.conv1 = Sequential(
    #         Conv2d(in_channels=3, out_channels=10, kernel_size=4, stride=2),
    #         LeakyReLU(),
    #         Conv2d(in_channels=10, out_channels=25, kernel_size=4, stride=1),
    #         MaxPool2d(2, 2, padding=0),
    #         LeakyReLU(),
    #         Conv2d(in_channels=25, out_channels=50, kernel_size=3, stride=1),
    #         MaxPool2d(4, 4, padding=0),
    #         LeakyReLU(),
    #     )
    #     self.linear = Sequential(
    #         Linear(50, 30),
    #         LeakyReLU(),
    #         Linear(30, 15),
    #     )

    # def forward(self, x):
    #     x = self.color(x)
    #     x = self.conv1(x)
    #     x = x.view(-1, 50)
    #     x = self.linear(x)
    #     return x
