# -*- coding: utf-8 -*-

from .....Functions.Plot.plot_3D_Data import plot_3D_Data as plot_3D_Data_fct
from .....Functions.init_fig import init_fig
from SciDataTool import VectorField


def plot_3D_Data(
    self,
    Data_str,
    *arg_list,
    component_list=None,
    is_norm=False,
    unit="SI",
    save_path=None,
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None,
    z_min=None,
    z_max=None,
    is_auto_ticks=True,
    is_2D_view=False,
    N_stem=100,
    fig=None,
):
    """Plots a field as a function of time

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
    *arg_list : list of str
        arguments to specify which axes to plot
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    save_path : str
        path and name of the png file to save
    x_min : float
        minimum value for the x-axis
    x_max : float
        maximum value for the x-axis
    y_min : float
        minimum value for the y-axis
    y_max : float
        maximum value for the y-axis
    z_min : float
        minimum value for the z-axis
    z_max : float
        maximum value for the z-axis
    is_auto_ticks : bool
        in fft, adjust ticks to freqs (deactivate if too close)
    is_2D_view : bool
        True to plot Data in xy plane and put z as colormap
    N_stem : int
        number of harmonics to plot (only for stem plots)
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    """

    # Get Data object names
    phys = getattr(self, Data_str.split(".")[0])
    data = getattr(phys, Data_str.split(".")[1])

    # Call the plot function
    if isinstance(data, VectorField):
        if component_list is None:  # default: extract all components
            component_list = data.components.keys()
        for i, comp in enumerate(component_list):
            (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")

            if save_path is not None:
                save_path_comp = (
                    save_path.split(".")[0] + "_" + comp + "." + save_path.split(".")[1]
                )
            else:
                save_path_comp = None

            plot_3D_Data_fct(
                data.components[comp],
                arg_list,
                is_norm=is_norm,
                unit=unit,
                save_path=save_path_comp,
                x_min=x_min,
                x_max=x_max,
                y_min=y_min,
                y_max=y_max,
                z_min=z_min,
                z_max=z_max,
                is_auto_ticks=is_auto_ticks,
                is_2D_view=is_2D_view,
                N_stem=N_stem,
                fig=fig,
            )

    else:
        (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")
        plot_3D_Data_fct(
            data,
            arg_list,
            is_norm=is_norm,
            unit=unit,
            save_path=save_path,
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max,
            z_min=z_min,
            z_max=z_max,
            is_auto_ticks=is_auto_ticks,
            is_2D_view=is_2D_view,
            N_stem=N_stem,
            fig=fig,
        )

    fig.show()