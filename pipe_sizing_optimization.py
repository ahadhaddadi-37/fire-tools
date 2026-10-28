# Pipe Sizing and Velocity Optimization Script for Fire Sprinkler Systems

def check_pipe_velocity(flow_gpm, pipe_diameter_inch, max_allowable_velocity_fps=20.0):
    """
    بررسی سرعت آب در لوله برای جلوگیری از ضربه قوچ و پدیده‌های فرسایشی
    فرمول سرعت: V = (0.4085 * Q) / (d^2)
    """
    if pipe_diameter_inch <= 0:
        raise ValueError("قطر لوله نامعتبر است.")
        
    # محاسبه سرعت بر حسب فوت بر ثانیه (fps)
    velocity_fps = (0.4085 * flow_gpm) / (pipe_diameter_inch ** 2)
    
    status = "Acceptable" if velocity_fps <= max_allowable_velocity_fps else "Warning: High Velocity!"
    
    return {
        "velocity_fps": round(velocity_fps, 2),
        "status": status
    }

# مثال کاربردی برای کاهش سایز لوله و بررسی سرعت:
if __name__ == "__main__":
    flow = 150.0  # دبی عبوری (GPM)
    diameters = [1.5, 2.0, 2.5]  # بررسی سایزهای مختلف لوله برای کاهش سایز بهینه
    
    print("نتایج بررسی سرعت جهت بهینه‌سازی و کاهش سایز لوله:")
    for d in diameters:
        result = check_pipe_velocity(flow, d)
        print(f"سایز لوله: {d} اینچ | سرعت جریان: {result['velocity_fps']} fps | وضعیت: {result['status']}")
