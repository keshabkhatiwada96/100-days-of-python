# # Virtual Environments and requirements.txt

# # 1. Create a virtual environment
# python -m venv .venv

# # 2. Activate the virtual environment
# .venv\Scripts\activate

# # 3. Check installed packages
# pip list

# # 4. Test whether requests is available
# python -c "import requests; print(requests.__version__)"

# # 5. Install requests
# pip install requests

# # 6. Create requirements.txt with installed packages
# pip freeze > requirements.txt

# # 7. Display requirements.txt
# type requirements.txt

# # 8. Install dependencies from requirements.txt
# pip install -r requirements.txt

# # 9. Uninstall requests
# pip uninstall requests

# # 10. Check installed packages again
# pip list

# # 11. Reinstall dependencies from requirements.txt
# pip install -r requirements.txt

# # 12. Check Git status
# git status

# # 13. Deactivate the virtual environment
# deactivate