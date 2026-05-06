import xarray as xr
import dask

def process_nasa_shocks(file_path):
    """
    Processes NASA MERRA-2 NetCDF4 arrays into 
    econometric-ready climate shocks.
    """
    # Lazy load 0.5-degree grid data
    ds = xr.open_dataset(file_path, chunks={'time': 12})

    # Calculate anomalies for the NASA-Bartik IV
    climatology = ds['T2M'].groupby("time.month").mean("time")
    anomalies = ds['T2M'].groupby("time.month") - climatology

    return anomalies
