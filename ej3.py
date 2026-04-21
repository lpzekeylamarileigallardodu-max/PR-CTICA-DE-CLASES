class distancia {
    public double x1 { get; set; }
    public double y1 { get; set; }
    public double x2 { get; set; }
    public double y2 { get; set; }

    public double obtenerDistancia() {
        double xd = Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2);
        double uwu = Math.Sqrt(xd);
        return uwu;
    }
}
