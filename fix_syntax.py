import glob, re

for filename in glob.glob('templates/admin*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # The block ends with:
    #                     options: {
    #                         responsive: true,
    #                         scales: {
    #                             y: { beginAtZero: true }
    #                         }
    #                     }
    #             }
    #     </script>
    
    # We need to replace it with:
    #                     options: {
    #                         responsive: true,
    #                         scales: {
    #                             y: { beginAtZero: true }
    #                         }
    #                     }
    #                 }); // Close Chart
    #             } // Close if(ctx)
    #         }); // Close DOMContentLoaded
    #     </script>

    html = re.sub(r'(\s*y: \{ beginAtZero: true \}\s*\n\s*\}\s*\n\s*\}\s*\n\s*)\}\s*\n\s*</script>', r'\1                });\n            }\n        });\n    </script>', html)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Syntax error fixed.")
