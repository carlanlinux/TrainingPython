class Duck:
    sound = 'Quuaaaaaaak!'
    walks = 'Walking like a duck'

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walks)


def main():
    donald = Duck()
    donald.quack()
    donald.walk()


if __name__ == '__main__':
    main()
