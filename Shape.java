
public class Shape {
    public double calculateArea() {
        return 0;
    }
}

class Rectangle extends Shape {
    double length;
    double width;

    Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    @Override
    public double calculateArea() {
        return length * width;
    }

    public double calculatePerimeter() {
        return 2 * (length + width);
    }
}

class Circle extends Shape {
    double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }

    public double calculateCircumference() {
        return 2 * Math.PI * radius;
    }
}

class Main {
    public static void main(String[] args) {

        Rectangle rect = new Rectangle(9, 5);
        System.out.println("=== Rectangle ===");
        System.out.println("Length      : " + rect.length);
        System.out.println("Width       : " + rect.width);
        System.out.println("Area        : " + rect.calculateArea());
        System.out.println("Perimeter   : " + rect.calculatePerimeter());

        System.out.println();

        Circle circle = new Circle(7);
        System.out.println("=== Circle ===");
        System.out.println("Radius          : " + circle.radius);
        System.out.println("Area            : " + String.format("%.2f", circle.calculateArea()));
        System.out.println("Circumference   : " + String.format("%.2f", circle.calculateCircumference()));
    }
}