# Hydraulic Calculation Engine for Sprinkler Systems (Hazen-Williams formula)

def calculate_friction_loss(flow_gpm, pipe_diameter_inch, length_ft, c_factor=120):
    """
    محاسبه افت اصطکاک لوله بر اساس فرمول حازن-ویلیامز مطابق با استانداردهای NFPA
    P = 4.52 * (Q^1.85) * (C^-1.85) * (d^-4.87) * L
    """
    if pipe_diameter_inch <= 0:
        raise ValueError("قطر لوله باید بزرگتر از صفر باشد.")
        
    # فرمول استاندارد حازن-ویلیامز برای سیستم‌های imperial/US units
    pressure_drop_psi = 4.52 * (flow_gpm ** 1.85) * (c_factor ** -1.85) * (pipe_diameter_inch ** -4.87) * length_ft
    return round(pressure_drop_psi, 4)

# مثال تست محاسباتی برای بررسی هوش مصنوعی:
if __name__ == "__main__":
    q = 250.0  # دبی بر حسب GPM
    d = 2.0    # قطر لوله بر حسب اینچ
    l = 100.0  # طول لوله بر حسب فوت
    c = 120    # ضریب زبری لوله فولادی (Schedule 40)
    
    loss = calculate_friction_loss(q, d, l, c)
    print(f"افت فشار محاسبه شده در لوله: {loss} PSI")
