image = [
    [1, 2, 4, 5, 6, 7],
    [1, 2, 7, 8, 9, 7],
    [1, 2, 4, 5, 6, 7],
    [1, 2, 4, 5, 6, 7],
    [1, 2, 4, 5, 6, 7],
    [1, 2, 4, 5, 6, 7],
    [1, 2, 4, 5, 6, 7],
    [1, 2, 4, 5, 6, 7],
    [1, 2, 4, 5, 6, 7],
    [1, 2, 4, 5, 6, 7],
]

template = [[4, 5, 6], [7, 8, 9]]

# Expected Output: [[0,2], [1,4]] # [start, end]

import numpy as np


class TemplateMatchingExample:
    def __init__(self, image):
        self.image = np.array(image)

    def match_template(self, template):
        """
        method matches given template in an image and returns position of row, col
        """

        image_rows, image_cols = np.shape(image)
        template_rows, template_cols = np.shape(template)
        print(template_rows, template_cols)
        zero_matrix = np.zeros((template_rows, template_cols))
        for row in range(0, image_rows - template_rows + 1):
            for col in range(0, image_cols - template_cols + 1):
                image_crop = self.image[row : row + template_rows][
                    col : col + template_cols
                ]
                difference_crop = np.array(image_crop) - np.array(template)
                if difference_crop == np.array(zero_matrix):
                    print(
                        "template found at:",
                        [[row, col], [row + template_rows, col, template_cols]],
                    )
                    return [[row, col], [row + template_rows, col, template_cols]]
        return [[-1, -1], [-1, -1]]


def main():
    matcher = TemplateMatchingExample(image)
    position = matcher.match_template(template)


main()
