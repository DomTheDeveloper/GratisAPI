"""Fundamental physical constants (CODATA recommended values)."""

META = {
    "name": "physical_constants",
    "title": "Physical Constants",
    "description": "Fundamental physical constants with symbols, values and units.",
    "emoji": "🔬",
}

# (id, name, symbol, value, unit, category)
_ROWS = [
    ("speed-of-light", "Speed of light in vacuum", "c", 299792458.0, "m/s", "Universal"),
    ("gravitational-constant", "Newtonian constant of gravitation", "G", 6.67430e-11, "m^3 kg^-1 s^-2", "Universal"),
    ("planck-constant", "Planck constant", "h", 6.62607015e-34, "J s", "Universal"),
    ("reduced-planck-constant", "Reduced Planck constant", "hbar", 1.054571817e-34, "J s", "Universal"),
    ("elementary-charge", "Elementary charge", "e", 1.602176634e-19, "C", "Electromagnetic"),
    ("vacuum-permeability", "Vacuum magnetic permeability", "mu_0", 1.25663706212e-6, "N A^-2", "Electromagnetic"),
    ("vacuum-permittivity", "Vacuum electric permittivity", "epsilon_0", 8.8541878128e-12, "F/m", "Electromagnetic"),
    ("coulomb-constant", "Coulomb constant", "k_e", 8.9875517873681764e9, "N m^2 C^-2", "Electromagnetic"),
    ("boltzmann-constant", "Boltzmann constant", "k_B", 1.380649e-23, "J/K", "Thermodynamic"),
    ("avogadro-constant", "Avogadro constant", "N_A", 6.02214076e23, "mol^-1", "Physicochemical"),
    ("gas-constant", "Molar gas constant", "R", 8.314462618, "J mol^-1 K^-1", "Physicochemical"),
    ("faraday-constant", "Faraday constant", "F", 96485.33212, "C/mol", "Physicochemical"),
    ("stefan-boltzmann-constant", "Stefan-Boltzmann constant", "sigma", 5.670374419e-8, "W m^-2 K^-4", "Thermodynamic"),
    ("electron-mass", "Electron mass", "m_e", 9.1093837015e-31, "kg", "Atomic"),
    ("proton-mass", "Proton mass", "m_p", 1.67262192369e-27, "kg", "Atomic"),
    ("neutron-mass", "Neutron mass", "m_n", 1.67492749804e-27, "kg", "Atomic"),
    ("atomic-mass-unit", "Atomic mass constant", "m_u", 1.66053906660e-27, "kg", "Atomic"),
    ("fine-structure-constant", "Fine-structure constant", "alpha", 7.2973525693e-3, "dimensionless", "Atomic"),
    ("rydberg-constant", "Rydberg constant", "R_inf", 10973731.568160, "m^-1", "Atomic"),
    ("bohr-radius", "Bohr radius", "a_0", 5.29177210903e-11, "m", "Atomic"),
    ("bohr-magneton", "Bohr magneton", "mu_B", 9.2740100783e-24, "J/T", "Atomic"),
    ("electron-volt", "Electron volt", "eV", 1.602176634e-19, "J", "Physicochemical"),
    ("standard-gravity", "Standard acceleration of gravity", "g_n", 9.80665, "m/s^2", "Adopted"),
    ("wien-displacement-constant", "Wien wavelength displacement law constant", "b", 2.897771955e-3, "m K", "Thermodynamic"),
    ("planck-mass", "Planck mass", "m_P", 2.176434e-8, "kg", "Universal"),
]

ITEMS = [
    {
        "id": _id,
        "name": name,
        "symbol": symbol,
        "value": value,
        "unit": unit,
        "category": category,
    }
    for (_id, name, symbol, value, unit, category) in _ROWS
]
