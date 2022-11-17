# This is a modified version of VolumeControl widget,
# Original source code: https://github.com/dildeolupbiten/VolumeControl

import tkinter as tk
from math import cos, sin, atan2, radians, degrees

class VolumeControl:

    def __init__(
            self,
            master: tk.Canvas,
            x: float,
            y: float,
            start: float,
            end: float,
            radius: float,
            length: float,
            width: float = 1.,
            distance: float = .0,
            text_height: float = 75,
            text_title: str = "Value: ",
            unit_color: str = "black",
            text_color: str = "white",
            needle_color: str = "grey",
            color_gradient: dict = None,
            integer: bool = False
    ):
        """
        "Construct a VolumeControl object with parent master.
        :param master: A canvas object.
        :param x: A float to determine the horizontal position of
                  the object.
        :param y: A float to determine the vertical position of
                  the object.
        :param start: A float that will be the start point of the
                      range where the needle will rotate.
        :param end: A float that will be the end point of the range
                    where the needle will rotate.
        :param radius: A float that will be the radius of the object.
        :param length: A float that determines the length of the
                       unit lines.
        :param width: A float for specifying the width of the lines.
        :param distance: A float that determines the distance of the
                         unit lines between the center and the edge and
                         also the length of the needle line.
        :param text_height: A float to determine the height of the text.
        :param text_title: A string that will be displayed under the object.
        :param unit_color: A string to determine the color of the
                           unit lines.
        :param needle_color: A string to determine the color of the needle
                             line
        :param color_gradient: A dictionary to specify which color gradient
                               will be used.
        """
        self.__master = master
        if color_gradient is None:
            self.__color_gradient = {"from": "yellow", "to": "red"}
        else:
            self.__color_gradient = color_gradient
        self.__x = (2 * x + radius) / 2
        self.__y = (2 * y + radius) / 2
        self.__needle_color = needle_color
        self.__text_height = text_height
        self.__text_title = text_title
        self.__unit_color = unit_color
        self.__text_color = text_color
        self.__distance = distance
        self.__length = length
        self.__width = width
        self.__start = start
        self.__end = end
        self.integer = integer
        self.__color_map = {
            ("yellow", "red"): (255, 1, 0, False),
            ("yellow", "green"): (1, 255, 0, False),
            ("pink", "blue"): (1, 0, 255, False),
            ("pink", "red"): (255, 0, 1, False),
            ("cyan", "green"): (0, 255, 1, False),
            ("cyan", "blue"): (0, 1, 255, False),
            ("red", "yellow"): (255, 1, 0, True),
            ("red", "pink"): (255, 0, 1, True),
            ("blue", "cyan"): (0, 1, 255, True),
            ("blue", "pink"): (1, 0, 255, True),
            ("green", "yellow"): (1, 255, 0, True),
            ("green", "cyan"): (0, 255, 1, True)
        }
        self.value = self.__start
        self.__status = True
        self.__palette = self.__create_palette()
        self.__create_needle()
        self.__create_units()
        self.__create_text()
        
    def __line_coordinates(self, r1: float, r2: float, angle: float) -> tuple:
        """
        This function is used for placing the lines around a circle.
        :param r1: Inner radius of the line
        :param r2: Outer radius of the line
        :param angle: Angle of the line
        :return: A tuple that contains 4 coordinates
        """
        return (
            self.__x + r1 * cos(radians(angle)),
            self.__y - r1 * sin(radians(angle)),
            self.__x + r2 * cos(radians(angle)),
            self.__y - r2 * sin(radians(angle))
        )

    @staticmethod
    def __rgb(r: int, g: int, b: int) -> str:
        """
        This function is used to create different colors.
        :param r: The integer value between 0 and 255 for red color
        :param g: The integer value between 0 and 255 for green color
        :param b: The integer value between 0 and 255 for blue color
        :return: A string that contains the rgb color code
        """
        return "#" + "".join(hex(i)[2:].zfill(2) for i in (r, g, b))

    @staticmethod
    def __select_color(color: int, index: int, reverse: bool = False) -> int:
        """
        This function is for determining which colors will be selected
        according to the color gradient.
        :param color: An integer that takes one of the values
                      from the list [0, 1, 255]
        :param index: An integer to calculate the color gradient of a single
                      unit line.
        :param reverse: A boolean value to reverse the color gradient
        :return: An integer for the color number of a single unit line.
        """
        color_number = index * 255 // 36
        if not reverse:
            color_number = 255 - color_number
        return color if color in [0, 255] else color_number

    def __create_palette(self) -> dict:
        """
        This function creates the color palette for
        each unit line. There are totally 36 unit lines
        and each unit line has a special tag and color.
        :return: A dictionary that contains the unit line tags and colors
        """
        unit_color = {}
        r, g, b, reverse = self.__color_map[
            tuple(self.__color_gradient.values())
        ]
        for index, i in enumerate(range(360, -1, -10)):
            unit_color[f"unit{i}"] = self.__rgb(
                r=self.__select_color(
                    color=r,
                    index=index,
                    reverse=reverse
                ),
                g=self.__select_color(
                    color=g,
                    index=index,
                    reverse=reverse
                ),
                b=self.__select_color(
                    color=b,
                    index=index,
                    reverse=reverse
                )
            )
        return unit_color

    def __create_units(self) -> None:
        """
        This function creates the unit lines.
        :return: None
        """
        for i in range(0, 360, 10):
            self.__master.create_line(
                self.__line_coordinates(
                    r1=self.__distance,
                    r2=(self.__distance + self.__length),
                    angle=i
                ),
                width=self.__width,
                tag=f"unit{i}",
                fill=self.__unit_color
            )

    def __create_needle(self) -> None:
        """
        This function creates the needle that can rotate.
        :return: None
        """
        self.__master.create_line(
            self.__line_coordinates(
                r1=0,
                r2=self.__distance,
                angle=0
            ),
            fill=self.__needle_color,
            width=self.__width,
            tag="needle"
        )
        self.__master.tag_bind(
            tagOrId="needle",
            sequence="<ButtonPress-1>",
            func=lambda event: self.__master.tag_bind(
                tagOrId="needle",
                sequence="<Motion>",
                func=self.__rotate_needle
            )
        )
        self.__master.tag_bind(
            tagOrId="needle",
            sequence="<ButtonRelease-1>",
            func=lambda event: self.__master.tag_unbind(
                tagOrId="needle",
                sequence="<Motion>"
            )
        )

    def __colorize(
            self,
            angle: float,
            start: int,
            end: int,
            color=""
    ) -> None:
        """
        This function changes the colors of the unit lines. The function
        is called first to change the colors of unit lines according to the
        selected color gradient, and second to change the colors of unit
        lines back to their original states.
        :param angle: A float number that shows the rotation angle.
        :param start: An integer number which means the start of the
                      range of unit lines which color will be changed.
        :param end: An integer number which means the end of the range of
                    unit lines which color will be changed.
        :param color: An empty string for removing the colored unit lines.
        :return:
        """
        if int(angle) == 0:
            pass
        elif int(angle) == 1:
            if color != self.__unit_color:
                color = self.__palette["unit0"]
            self.__master.itemconfig(tagOrId="unit0", fill=color)
        else:
            for i in range(start, end):
                if i != 0 and i % 10 == 0:
                    if color != self.__unit_color:
                        color = self.__palette[f"unit{i}"]
                    self.__master.itemconfig(tagOrId=f"unit{i}", fill=color)

    def __rotate_needle(self, event) -> None:
        """
        This function rotates the needle, calls the colorizing function and
        changes the value of the text.
        :param event: A tkinter event
        :return: None
        """
        angle = degrees(atan2(self.__y - event.y, event.x - self.__x))
        if angle < 0:
            angle += 360
        if (
                angle < 90 and self.__status
                or
                angle > 270 and not self.__status
        ):
            angle = 0
        if 0 < angle < 180:
            self.__status = False
        elif 180 < angle < 360:
            self.__status = True
        if self.integer==False:
            self.value = round(
                (self.__end - self.__start) / 360 * (360 - angle) + self.__start,
                2
            )
        else:
            self.value = int(round(
                (self.__end - self.__start) / 360 * (360 - angle) + self.__start,
                0
            ))
        if self.value == self.__end and self.__status:
            self.value = self.__start
        self.__master.coords(
            "needle",
            self.__line_coordinates(
                r1=0,
                r2=self.__distance,
                angle=angle
            )
        )
        self.__colorize(angle=angle, start=int(angle), end=360)
        self.__colorize(
            angle=angle,
            start=0,
            end=int(angle),
            color=self.__unit_color
        )
        if self.integer==False:
            self.__master.itemconfigure(
                tagOrId="value",
                text=f"{self.__text_title}{self.value}"
            )
        else:
            self.__master.itemconfigure(
                tagOrId="value",
                text=f"{self.__text_title}{int(self.value)}"
            )

    def __create_text(self) -> None:
        """
        A function that creates a text object to show what
        the value of the position of needle is.
        :return: None
        """
        self.__master.create_text(
            self.__x,
            self.__y + self.__text_height, fill=self.__text_color,
            text=f"{self.__text_title}{int(self.value)}",
            tag="value"
        )
