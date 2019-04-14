from view.flymap_editor import FlymapEditor
from controller import towns as controller
from controller import files as file_controller


def main():
    app = FlymapEditor()

    controller.init(app)
    file_controller.open_towns()

    app.mainloop()


if __name__ == '__main__':
    main()
