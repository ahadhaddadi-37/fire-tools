import ezdxf

def analyze_fire_protection_dxf(file_path):
    try:
        # بارگذاری فایل DXF نقشه
        doc = ezdxf.readfile(file_path)
        msp = doc.modelspace()
        
        print(جستجوی لایه‌ها و المان‌های سیستم اطفا حریق در فایل: {file_path})
        
        # شمارش لایه‌ها و موجودیت‌ها
        layers = doc.layers
        print(f"تعداد کل لایه‌ها (Layers): {len(layers)}")
        
        # بررسی بلوک‌ها (برای یافتن اسپرینکلرها، شیرآلات و تجهیزات)
        blocks = doc.blocks
        print(f"تعداد بلوک‌های تعریف شده: {len(blocks)}")
        
        # استخراج متن‌ها (مانند مشخصات لوله‌ها، سایزها و تگ‌ها)
        text_count = 0
        for entity in msp:
            if entity.dxftype() in ['TEXT', 'MTEXT']:
                text_count += 1
                # می‌توان متن‌های مربوط به سایز لوله یا نوع اسپرینکلر را فیلتر کرد
        
        print(f"تعداد متون موجود در مدل‌سِپیس: {text_count}")
        print("تحلیل اولیه فایل با موفقیت انجام شد.")
        
    except IOError:
        print(f"خطا: فایل {file_path} پیدا نشد یا قابل خواندن نیست.")
    except ezdxf.DXFStructureError:
        print("خطا: ساختار فایل DXF معتبر نیست.")

# نمونه نحوه استفاده:
# analyze_fire_protection_dxf("sprinkler_plan.dxf")
