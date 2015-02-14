#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Jan 20 22:52:35 2015
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 50000
        self.Phase_0 = Phase_0 = 90
        self.Freq_0 = Freq_0 = 500
        self.Amp_0 = Amp_0 = 50

        ##################################################
        # Blocks
        ##################################################
        _samp_rate_sizer = wx.BoxSizer(wx.VERTICAL)
        self._samp_rate_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_samp_rate_sizer,
        	value=self.samp_rate,
        	callback=self.set_samp_rate,
        	label='samp_rate',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._samp_rate_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_samp_rate_sizer,
        	value=self.samp_rate,
        	callback=self.set_samp_rate,
        	minimum=0,
        	maximum=100000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_samp_rate_sizer)
        _Phase_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._Phase_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_Phase_0_sizer,
        	value=self.Phase_0,
        	callback=self.set_Phase_0,
        	label='Phase_0',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._Phase_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_Phase_0_sizer,
        	value=self.Phase_0,
        	callback=self.set_Phase_0,
        	minimum=0,
        	maximum=360,
        	num_steps=360,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_Phase_0_sizer)
        _Freq_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._Freq_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_Freq_0_sizer,
        	value=self.Freq_0,
        	callback=self.set_Freq_0,
        	label='Freq_0',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._Freq_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_Freq_0_sizer,
        	value=self.Freq_0,
        	callback=self.set_Freq_0,
        	minimum=0,
        	maximum=1000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_Freq_0_sizer)
        _Amp_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._Amp_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_Amp_0_sizer,
        	value=self.Amp_0,
        	callback=self.set_Amp_0,
        	label='Amp_0',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._Amp_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_Amp_0_sizer,
        	value=self.Amp_0,
        	callback=self.set_Amp_0,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_Amp_0_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, Phase_0, Amp_0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, Phase_0, Amp_0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, Freq_0, Amp_0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, Freq_0, Amp_0, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self._samp_rate_slider.set_value(self.samp_rate)
        self._samp_rate_text_box.set_value(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

    def get_Phase_0(self):
        return self.Phase_0

    def set_Phase_0(self, Phase_0):
        self.Phase_0 = Phase_0
        self._Phase_0_slider.set_value(self.Phase_0)
        self._Phase_0_text_box.set_value(self.Phase_0)
        self.analog_sig_source_x_0_1.set_frequency(self.Phase_0)
        self.analog_sig_source_x_0_0_0.set_frequency(self.Phase_0)

    def get_Freq_0(self):
        return self.Freq_0

    def set_Freq_0(self, Freq_0):
        self.Freq_0 = Freq_0
        self._Freq_0_slider.set_value(self.Freq_0)
        self._Freq_0_text_box.set_value(self.Freq_0)
        self.analog_sig_source_x_0.set_frequency(self.Freq_0)
        self.analog_sig_source_x_0_0.set_frequency(self.Freq_0)

    def get_Amp_0(self):
        return self.Amp_0

    def set_Amp_0(self, Amp_0):
        self.Amp_0 = Amp_0
        self._Amp_0_slider.set_value(self.Amp_0)
        self._Amp_0_text_box.set_value(self.Amp_0)
        self.analog_sig_source_x_0.set_amplitude(self.Amp_0)
        self.analog_sig_source_x_0_1.set_amplitude(self.Amp_0)
        self.analog_sig_source_x_0_0.set_amplitude(self.Amp_0)
        self.analog_sig_source_x_0_0_0.set_amplitude(self.Amp_0)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()

