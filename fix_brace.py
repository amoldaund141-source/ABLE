import re

with open('static/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# We need to remove the extra closing brace that was injected.
# The code looks like this:
#         } catch (e) {
#             console.error("Error loading volunteers:", e);
#         }
#     }
# }
# 
#     // Admin Reports

target = """        } catch (e) {
            console.error("Error loading volunteers:", e);
        }
    }
}

    // Admin Reports"""

replacement = """        } catch (e) {
            console.error("Error loading volunteers:", e);
        }
    }

    // Admin Reports"""

js = js.replace(target, replacement)

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Removed premature closing brace!")
