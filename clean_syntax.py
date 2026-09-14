for filename in ['templates/admin.html', 'templates/user-dashboard.html', 'templates/volunteer-dashboard.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    out_lines = []
    skip = False
    for line in lines:
        if line.strip() == '<script>':
            out_lines.append(line)
            continue
            
        # If we see the broken closing brackets right after <script>, we skip them
        if line.strip() in ['}', '});'] and out_lines[-1].strip() == '<script>':
            continue
        if line.strip() == '});' and out_lines[-1].strip() == '}':
            continue

        out_lines.append(line)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)

print("Syntax errors cleaned.")
