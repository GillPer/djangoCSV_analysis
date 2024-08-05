from django.shortcuts import render
from .forms import UploadFileForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import urllib, base64

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_csv(file)


            head = df.head().to_html()
            describe = df.describe().to_html()
            missing_values = df.isnull().sum().to_dict()

            # Data visualization
            img = io.BytesIO()
            sns.histplot(df.select_dtypes(include=np.number).iloc[:, 0]).figure.savefig(img, format='png')
            img.seek(0)
            plot_url = urllib.parse.quote(base64.b64encode(img.read()).decode())

            context = {
                'columns': df.columns,
                'head': head,
                'describe': describe,
                'missing_values': missing_values,
                'plot_url': plot_url
            }
            return render(request, 'analysis/results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})

