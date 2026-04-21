class Triangulo {
    public double lado1 { get; set; }
    public double lado2 { get; set; }
    public double lado3 { get; set; }

    public double calcularArea() {
        double xd = (lado1 + lado2 + lado3) / 2;
        double uwu = Math.Sqrt(xd * (xd - lado1) * (xd - lado2) * (xd - lado3));
        return uwu;
    }
}
