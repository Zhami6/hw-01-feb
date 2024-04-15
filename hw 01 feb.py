from __future__ import annotations


class ComplexNumber:
    def __init__(self, real: int, img: int) -> None:
        self.real = real
        self.img = img

    def __add__(self, cx: ComplexNumber) -> ComplexNumber:
        """Сложение комплексных чисел."""
        new_real = self.real + cx.real
        new_img = self.img + cx.img
        return ComplexNumber(new_real, new_img)

    def __sub__(self, cx: ComplexNumber) -> ComplexNumber:
        """Вычитание комплексных чисел."""
        new_real = self.real - cx.real
        new_img = self.img - cx.img
        return ComplexNumber(new_real, new_img)

    def __repr__(self) -> str:
        """Строковое представление комплексного числа."""
        return f"{self.real} {'+' if self.img >= 0 else '-'} {abs(self.img)}i"

    def __iadd__(self, cx: ComplexNumber) -> ComplexNumber:
        """Инкрементное сложение."""
        self.real += cx.real
        self.img += cx.img
        return self

    def __isub__(self, cx: ComplexNumber) -> ComplexNumber:
        """Инкрементное вычитание."""
        self.real -= cx.real
        self.img -= cx.img
        return self

    def __eq__(self, cx: ComplexNumber) -> bool:
        """Сравнение комплексных чисел."""
        return self.real == cx.real and self.img == cx.img


cx1 = ComplexNumber(3, 4)
cx2 = ComplexNumber(1, 2)
print(cx1 + cx2)
print(cx1 - cx2)
cx1 += cx2
print(cx1)
cx1 -= cx2
print(cx1)
print(cx1 == cx2)
cx3 = ComplexNumber(3, 4)
print(cx1 == cx3)
