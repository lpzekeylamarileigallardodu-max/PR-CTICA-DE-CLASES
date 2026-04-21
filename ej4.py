class Auto {
    public double costoBase { get; set; }

    public double costoTotal() {
        double xd = costoBase * 1.12; 
        double uwu = xd * 1.06;   

        return uwu;
    }
}
