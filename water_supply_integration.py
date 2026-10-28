# Water Supply and System Demand Analysis Script for Fire Sprinkler Systems

def check_water_supply_adequacy(available_flow_gpm, available_pressure_psi, required_flow_gpm, required_pressure_psi):
    """
    بررسی تطبیق دبی و فشار منبع آب (یا پمپ) با نیاز محاسباتی سیستم اسپرینکلر
    مطابق با استانداردهای تحلیل هیدرولیکی NFPA
    """
    flow_adequate = available_flow_gpm >= required_flow_gpm
    pressure_adequate = available_pressure_psi >= required_pressure_psi
    
    status = "Approved: Water supply meets system demand."
    recommendations = []
    
    if not flow_adequate:
        recommendations.append("دبی منبع آب کمتر از میزان مورد نیاز است. به پمپ یا منبع بزرگتری نیاز است.")
    if not pressure_adequate:
        recommendations.append("فشار منبع آب کمتر از حد نیاز است. افزایش فشار پمپ (Boost) الزامی است.")
        
    if not flow_adequate or not pressure_adequate:
        status = "Warning: Water supply deficient! Design review required."
        
    return {
        "status": status,
        "flow_adequate": flow_adequate,
        "pressure_adequate": pressure_adequate,
        "recommendations": recommendations
    }

# مثال کاربردی برای ارزیابی منبع آب پروژه:
if __name__ == "__main__":
    # مقادیر دبی و فشار موجود منبع/پمپ
    avail_flow = 500.0   # GPM
    avail_press = 85.0   # PSI
    
    # مقادیر دبی و فشار مورد نیاز محاسباتی شبکه اسپرینکلر
    req_flow = 400.0     # GPM
    req_press = 65.0     # PSI
    
    result = check_water_supply_adequacy(avail_flow, avail_press, req_flow, req_press)
    print(f"وضعیت تأمین آب: {result['status']}")
    if result['recommendations']:
        print("توصیه‌های مهندسی:", result['recommendations'])
    else:
        print("سیستم از نظر تامین فشار و دبی در وضعیت مطلوب قرار دارد.")
