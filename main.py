"""
A convenient wrapper on git

todo:
    check if a url has been loaded, open its folder
    handle trailing slashes
    0Oo1lL
"""

from typing import Tuple
import subprocess, os

import pyperclip as pc, send2trash as stt

from sl4ng import mainame, pop, show, getsource, clean_url, flat
from filey import mcd


here, this = os.path.split(__file__)


def initialize_Logger(urls:str, path:str='log.pkl', clear=True) -> bool:
    """
    Initialize a Logger with a collection (multiline string or iterable of strings) of urls you had previously downloaded
    Return True if the Logger has the same number of elements as the mlstring had resource locators
    If the Logger exists and is non-empty, the specified urls will be added to the "start" of the log, and all remainers will be re-added afterwards
    The logger will only include the first copy of any string.
    params
        path
            string of the path to the log you would like to initialize
        urls
            string, or multiline string, of urls separated by spaces, and/or new lines.
        clear
            whether or not to erase the Logger from storage if it already exists
    """
    os.remove(path) if os.path.exists(path) and clear else None
    urls = urls if isinstance(urls, str) else ' '.join(urls) 
    log = Logger(path=path, kind=str)
    
    current_elements = [*log] if log.exists else []
    
    urls = [*map(str.strip, urls.split())] + current_elements
    
    show(map(log.update, map(clean_url, urls)))
    
    return log


def username(url:str) -> tuple:
    user, name = url.split('/')[-2:]
    return user, name[:-4]
    
def locator(url):
    url = clean_url(url)    
    _git = '.git'
    return url if url.endswith(_git) else url + _git
    
def path(url):
    uri = locator(url)
    user, name = username(uri)
    folder = os.path.join(here, "clones", user, name)
    return folder



def clone(url:str, pop:bool=True, copy:bool=False) -> str:
    """
    Clone a repository and update the log
    param
        pop
            choose whether or not to open the directory after cloning
        copy
            choose whether or not to copy the directory's path after cloning
    """
    origin = os.getcwd()
    
    uri = locator(url)
    
    # user, name = username(uri)
    # folder = os.path.join(here, "clones", user) 
    folder = path(uri)
    mcd(os.path.dirname(folder), overwrite=True) # create author's directory
    # os.chdir(folder)
    
    subprocess.run(f"git clone {uri}") # cloning in
    
    os.chdir(origin)
    
    # log.update(url)
    
    if pop:
        os.startfile(folder) 
    if copy:
        pc.copy(folder)
    return folder



def batch(urls:str, pop:bool=True, sep:str=','):
    users = {clone(url, pop) for url in urls.split(sep)}
    return users

def main(urls, pop:bool=False, copy:bool=False):
    """
    Parse a multiline string or iterator with resource locators and clone each one into dirname(__file__)/clones/user_name/repository_name
    """
    if isinstance(urls, list):
        # show(map(clone, url))
        pass
    elif isinstance(urls, str):
        if ' ' in urls:
            # show(map(clone, url.split()))
            urls = urls.split()
        else:
            # print(clone(url))
            urls = [urls]
    for i, url in enumerate(urls, 1):
        print('%d of %d' % (i, len(urls)))
        
        # if not (os.path.exists(path(url)) or clean_url(url) in log):
        print(clone(url, copy=copy, pop=pop))
        print('\n' * 4)



if __name__ == '__main__':
    urls = """
    https://github.com/akapkotel/light_raycasting.git
    https://github.com/cls1991/ng.git
    https://github.com/DinoZ1729/Ray.git
    https://github.com/DinoZ1729/Earth
    https://github.com/DinoZ1729/Tetris
    https://github.com/DinoZ1729/Game
    https://github.com/DinoZ1729/Double-Pendulum
    https://github.com/DinoZ1729/Galaxy
    https://github.com/mikedh/trimesh https://github.com/Toblerity/Shapely https://github.com/mmatl/pyrender
    https://tildegit.org/solderpunk/AV-98.git
    https://github.com/MasterQ32/kristall.git
    https://github.com/makeworld-the-better-one/amfora
    https://tildegit.org/sloum/bombadillo
    https://github.com/mbrubeck/agate/
    https://tildegit.org/sloum/chalk
    https://tildegit.org/sloum/lid
    https://tildegit.org/fluora/interval.rs
    https://github.com/tildeclub/tilde.club
    https://tildegit.org/fluora/modu https://tildegit.org/fluora/irradiate https://tildegit.org/fluora/hecc https://tildegit.org/sloum/filtress
    https://git.skyjake.fi/skyjake/lagrange
    https://github.com/karpathy/char-rnn https://github.com/audiodude/neural-noise https://tildegit.org/tildeverse/zine
    https://github.com/NeuralNine/vidstream
    https://github.com/anime-dl/anime-downloader
    https://github.com/mpv-player/mpv
    https://github.com/boppreh/keyboard
    https://github.com/boppreh/mouse
    https://github.com/librosa/librosa
    https://github.com/hfeeki/termcolor
    https://github.com/jackmaney/python-stdlib-list
    https://github.com/giampaolo/psutil
    https://github.com/psf/requests
    https://github.com/lucasmlofaro/cabinets
    https://github.com/boisgera/bitstream https://github.com/EliosMolina/audio_degrader https://github.com/hassaku/audio-plot https://github.com/psf/black https://github.com/vipul-sharma20/audio-mouse https://github.com/wiccy46/audio2numpy https://github.com/LG-1/audio2text
    https://github.com/KoffeinFlummi/ext https://github.com/google/snappy
    https://github.com/jmurty/xml4h
    https://github.com/tesseract-ocr/tesseract
    https://github.com/microsoft/vcpkg
    https://github.com/wingtk/gvsbuild
    https://github.com/tesseract-ocr/tessdata_fast/blob/master/eng.traineddata https://github.com/tesseract-ocr/tessdata_best/blob/master/eng.traineddata
    https://github.com/tesseract-ocr/tessdata_fast https://github.com/tesseract-ocr/tessdata_best
    https://github.com/w0rthy/SortingVisualizer
    https://github.com/zdenop/tessdata_downloader
    https://github.com/Arvintian/madara
    https://github.com/shpaker/wifi_qrcode https://github.com/lincolnloop/python-qrcode
    https://github.com/madmaze/pytesseract
    https://github.com/clementmihailescu/Pathfinding-Visualizer https://github.com/clementmihailescu/Pathfinding-Visualizer-Tutorial https://github.com/clementmihailescu/Oak-Programming-Language
    https://github.com/JuliaCrypto/OpenSSH.jl https://github.com/paramiko/paramiko https://github.com/bongtrop/digit
    https://github.com/joel-simon/ganbreeder
    https://github.com/niklasf/python-chess
    https://github.com/baliksjosay/audio_recogition_system
    https://github.com/drager/faker https://github.com/joke2k/faker
    https://github.com/nucleic/enaml
    https://github.com/numba/numba
    https://github.com/75lb/ansi-escape-sequences
    https://github.com/Infinidat/infi.systray https://github.com/bastibe/SoundCard
    https://github.com/gdemos01/crypto-trading-ai-bot-basic
    https://github.com/ilanschnell/bitarray
    https://gitlab.com/RebelCoder/dna-toolset
    https://github.com/mcfletch/pyopengl https://github.com/mcfletch/openglcontext
    https://github.com/JulienPalard/oeis https://github.com/sidneycadot/oeis
    https://github.com/DanChitwood/PlantsAndPython
    https://github.com/UN-GCPDS/qt-material
    https://github.com/shunsvineyard/pyforest
    https://github.com/codelucas/cracking-the-da-vinci-code-with-google-interview-problems-and-nlp-in-python
    https://github.com/xapple/fasta
    https://github.com/elliotwaite/rule-30-and-game-of-life
    https://github.com/elliotwaite/times-table-animation
    https://github.com/xapple/autopaths
    https://github.com/treeform/steganography
    https://github.com/elliotwaite/pycairo-animations
    https://github.com/kroitor/asciichart
    https://github.com/kblin/ncbi-genome-download
    https://github.com/evanjs/iTunesCLI https://github.com/evanjs/hydrus https://github.com/evanjs/licensor
    https://github.com/h2non/filetype.py https://github.com/pyGrowler/Growler
    https://github.com/wummel/patool
    https://github.com/thebigmunch/audio-metadata
    https://github.com/iheanyi/bandcamp-dl https://github.com/Miserlou/SoundScrape https://github.com/iheanyi/Maya-Rain-Generator-Script https://github.com/Miserlou/chords2midi https://github.com/Miserlou/Trapify https://github.com/Miserlou/Vape https://github.com/Miserlou/Emo https://github.com/Miserlou/Zalgo https://github.com/Miserlou/omnihash https://github.com/Miserlou/nogoogle
    https://github.com/noffle/art-of-readme
    https://github.com/microsoft/WSL2-Linux-Kernel
    https://github.com/wonsjb/MusicGenerator https://github.com/lordmauve/gamemaths https://github.com/lordmauve/heightfield https://github.com/lawsie/guizero https://github.com/bspaans/python-mingus https://github.com/exaile/exaile
    https://github.com/marl0ny/QM-Simulator-1D https://github.com/marl0ny/file-scripts https://github.com/benmaier/reaction-diffusion https://github.com/marl0ny/colourful-sound-bars https://github.com/jwkvam/celluloid https://github.com/daniel-s-ingram/ai_for_robotics https://github.com/marl0ny/grids-on-the-complex-plane https://github.com/marl0ny/slidy-plotty-graphy https://github.com/0xflotus/ip2d https://github.com/asweigart/stdiomask https://github.com/asweigart/divisonbeads https://github.com/robertmartin8/PyGameofLife https://github.com/asweigart/squintmaze https://github.com/asweigart/PyTextCanvas https://github.com/pavankalyan1997/Machine-learning-without-any-libraries https://github.com/TobyBoyne/fourier-animation https://github.com/pavankalyan1997/GenderFromNames https://github.com/asweigart/mondrian_art_generator https://github.com/asweigart/pysimplevalidate https://github.com/asweigart/pyganim https://github.com/asweigart/art-of-turtle-programming https://github.com/asweigart/shortstr https://github.com/asweigart/PyMsgBox https://github.com/asweigart/nicewin https://github.com/asweigart/pyfuzzybool https://github.com/asweigart/mouseinfo https://github.com/asweigart/codebreaker https://github.com/asweigart/ezgmail https://github.com/TobyBoyne/major-system https://github.com/NakahodoRintaro/Trocoid_animation https://github.com/xhguleixin123/Cellular-Automata https://github.com/Doormango/lambda-calc/blob/master/lambda-calc.py https://github.com/karan-owalekar/Visualize-Sorting-Algorithms https://github.com/KasiChennupati/DepositionModels
    https://github.com/mkorman90/regipy https://github.com/shpaker/winregistry https://github.com/maxhumber/gif https://github.com/bjodah/chempy https://swiftshader.googlesource.com/SwiftShader https://chromium.googlesource.com/angle/angle
    https://github.com/Wanderson-Magalhaes/Simple_PySide_Base
    https://github.com/mrexodia/pygame_qt
    https://github.com/khvmaths/DinoRun-PyQt-PyGame
    https://github.com/jgthms/web-design-in-4-minutes
    https://github.com/jgthms/bulma
    https://github.com/jgthms/bulma-start
    https://github.com/MicrosoftDocs/PowerShell-Docs
    https://github.com/keithito/tacotron
    https://github.com/brentvollebregt/auto-py-to-exe
    https://github.com/benawad/vstodo
    https://github.com/beurtschipper/Depix
    """
    # logpath = os.path.join(here, 'log.pkl')
    # log = initialize_Logger(urls, logpath, True)
    # log = initialize_Logger(urls, logpath, False)
    # log = Logger(kind=str)
    # initialize_Logger(urls)
    urls = "https://github.com/jgthms/marksheet https://github.com/jgthms/css-reference https://github.com/jgthms/html-reference https://github.com/jgthms/javascript-in-14-minutes"
    urls = 'https://github.com/less/less-docs/'
    urls = 'https://github.com/jgthms/wysiwyg.css'
    urls = 'https://github.com/lydell/resolve-url'
    urls = 'https://github.com/howCodeORG/Simple-Python-Blockchain'
    # urls = 'https://github.com/Eloston/ungoogled-chromium https://github.com/chromium/chromium https://github.com/brython-dev/brython https://github.com/qutebrowser/qutebrowser'
    urls = 'https://github.com/Eloston/ungoogled-chromium https://github.com/brython-dev/brython https://github.com/qutebrowser/qutebrowser https://github.com/chromium/chromium'
    urls = 'https://gitlab.com/pgjones/quart https://github.com/vibora-io/vibora https://github.com/tiangolo/typer https://github.com/tornadoweb/tornado https://github.com/AstroMatt/book-python https://github.com/tiangolo/fastapi'
    urls = 'https://github.com/pygments/pygments https://github.com/iodide-project/pyodide https://github.com/flutter/website'
    urls = 'https://github.com/nauaneeth/colour-randomizer https://github.com/nauaneeth/nauaneeth.github.io https://github.com/nauaneeth/alternaet.github.io https://github.com/Infinidat/infi.systray https://github.com/varunnaik/PaletteViewer https://github.com/apoorvaeternity/colory'
    
    
    urls = 'https://github.com/MicrosoftDocs/terminal https://github.com/echosa/gopher-php https://github.com/zenshinji/gopher-parser https://github.com/fireice-uk/xmr-stak https://github.com/kr1sp1n/awesome-gemini https://github.com/makeworld-the-better-one/amfora https://github.com/mbrubeck/agate https://github.com/pitr/gemini-ios https://github.com/makeworld-the-better-one/gemget https://github.com/cbrews/ignition https://github.com/alexwennerberg/flounder'
    urls = 'https://github.com/loadingio/css-spinner https://github.com/englercj/resource-loader'
    urls = 'https://github.com/ProjectOpenSea/opensea-creatures https://github.com/ethereum/remix-live'
    urls = 'https://github.com/ILXL-guides/dynamic_memory_allocation https://github.com/ILXL-guides/cpp-file-io https://github.com/ILXL-guides/function-file-organization https://github.com/ILXL-guides/arrays-as-parameters https://github.com/ILXL-guides/object-parameters-and-return-values https://github.com/ILXL-guides/intro-to-graphics https://github.com/ILXL-guides/cplusplus-getline-tutorials https://github.com/ILXL-guides/intro-to-graphics https://github.com/ILXL-guides/command-line-treasure-hunt https://github.com/ILXL-guides/intro-to-karel'
    urls = 'https://github.com/mdn/content'
    urls = 'https://github.com/dabeaz/ply https://github.com/alex/rply'
    urls = 'https://github.com/rst2pdf/rst2pdf'
    urls = 'https://github.com/wereturtle/ghostwriter'
    urls = 'https://github.com/steinbergmedia/vstgui https://github.com/steinbergmedia/vst3_pluginterfaces https://github.com/steinbergmedia/vst3_public_sdk https://github.com/steinbergmedia/vst3sdk https://github.com/steinbergmedia/vst3_doc https://github.com/steinbergmedia/smufl'
    urls = 'https://github.com/rayon-rs/rayon https://github.com/nwtgck/ray-tracing-iow-rust https://github.com/rust-lang/book https://github.com/rust-lang/mdBook https://github.com/udhos/update-golang'
    urls = 'https://github.com/arsenetar/send2trash'
    urls = 'https://bitbucket.org/mrabarnett/mrab-regex.git'
    urls = 'https://github.com/Martinsos/edlib'
    urls = 'https://github.com/miku/binpic https://github.com/carbon-app/carbon https://github.com/buchanae/ink github.com/Aloxaf/silicon github.com/miku/binpic github.com/qeesung/image2ascii github.com/eleby/pixelizer github.com/buchanae/ink'
    urls = 'https://github.com/kendfss/kendfss.github.io.git https://github.com/gjtorikian/markdowntutorial.com'
    urls = 'https://github.com/fossasia/searss https://github.com/wking/rss2email https://github.com/kurtmckee/feedparser https://github.com/Alir3z4/html2text https://github.com/SlyMarbo/rss https://github.com/ch3rc/DIP5 https://gitlab.gnome.org/GNOME/gimp https://github.com/akkana/gimp-plugins https://github.com/kritiksoman/GIMP-ML https://github.com/doctormo/GimpPs https://github.com/BenChallenor/lomography'
    # urls = 'github.com/Aloxaf/silicon github.com/miku/binpic github.com/qeesung/image2ascii github.com/eleby/pixelizer github.com/buchanae/ink'
    
    urls = 'https://github.com/asottile/setuptools-golang'
    urls = 'github.com/eleby/pixelizer https://github.com/matsuyoshi30/germanium github.com/kdomanski/iso9660 https://github.com/buchanae/ink https://github.com/glfw/glfw github.com/jdxyw/generativeart '
    urls = 'https://github.com/tj/letterbox https://github.com/fogleman/gorgb https://github.com/h2non/bimg https://github.com/libvips/libvips https://github.com/dbkaplun/allrgb https://github.com/fogleman/AllRGB https://github.com/dcgoings/allRGB'
    urls = 'https://github.com/golang/mobile https://github.com/jdxyw/generativeart'
    urls = 'https://github.com/qeesung/image2ascii'
    urls = 'https://github.com/hhatto/nude.py https://github.com/koyachi/go-nude'
    urls = 'https://github.com/jankais3r/Recolor'
    urls = 'https://github.com/FFmpeg/FFmpeg https://github.com/tuxu/python-samplerate https://github.com/gabriel-vasile/mimetype'
    urls = 'https://github.com/aferriss/p5jsShaderExamples https://github.com/benawad/dogehouse https://github.com/benawad/react-conway-game-of-life https://github.com/meyda/meyda https://github.com/processing/p5.js'
    urls = 'https://github.com/DavidLazic/audio-visualizer'
    urls = 'https://github.com/thebigmunch/tbm-utils https://github.com/Martinsos/edlib'
    urls = 'https://github.com/makinteractlab/p5.js-templates https://github.com/mshmoustafa/oeisclient https://github.com/heldersepu/nppfavorites https://github.com/TaylorSMarks/playsound'
    urls = 'https://github.com/processing/p5.js-website'
    urls = 'https://github.com/rkulla/pydiction.git https://github.com/doxygen/doxygen.git'
    urls = 'https://github.com/zhiwehu/Python-programming-exercises'
    urls = 'https://github.com/brython-dev/brython'
    urls = 'https://github.com/brython-dev/brython-pygame'
    urls = 'https://github.com/fyne-io/developer.fyne.io'
    urls = 'https://classic.yarnpkg.com/en/docs/install'
    urls = 'https://github.com/Maddoc42/Android-Material-Icon-Generator https://github.com/onmyway133/IconGenerator https://github.com/redbooth/free-file-icons'
    urls = 'https://github.com/weslly/ColorPicker https://github.com/chrisbliss18/php-ico https://github.com/hamzaafridi/icon-generator'
    urls = 'https://github.com/flutter/website'
    urls = 'https://github.com/nvm-sh/nvm https://github.com/rvm/rvm https://github.com/microsoft/vscode-docs https://github.com/notepad-plus-plus/notepad-plus-plus https://github.com/notepad-plus-plus/npp-usermanual https://github.com/notepad-plus-plus/userDefinedLanguages https://github.com/bruderstein/PythonScript https://github.com/bitagoras/PyPadPlusPlus https://github.com/asweigart/virtualclapperboard'
    urls = 'https://github.com/skybrian/dart-synth-demo https://github.com/ronak197/visualizer https://github.com/modulovalue/flutter_audio_wav_demo https://github.com/gkvoelkl/python-sonic https://github.com/sonic-pi-net/sonic-pi https://github.com/pdrb/dbj https://github.com/SpotlightKid/python-rtmidi https://github.com/stephwag/midi-text https://github.com/vishnubob/python-midi https://github.com/attwad/python-osc https://github.com/lebaston100/MIDItoOBS https://github.com/msiemens/tinydb'
    urls = 'https://gitlab.freedesktop.org/pkg-config/pkg-config'
    urls = 'https://github.com/agraef/purr-data'
    urls = 'https://github.com/4383/barcode https://github.com/jfjlaros/barcode'
    urls = 'https://github.com/kendfss/barcode'
    urls = 'https://github.com/fristonio/g-Ignore'
    urls = 'https://github.com/github/gitignore.git'
    urls = 'https://github.com/canadaduane/elm-hccb'
    urls = 'https://github.com/kata198/mdToRst'
    urls = 'https://github.com/FlutterOpen/flutter-canvas https://github.com/rxlabz/flutter_canvas_to_image https://github.com/brendan-duncan/image https://github.com/lykhonis/image_crop https://github.com/edx/mdrst https://github.com/tshedor/flutter_image_form_field'
    urls = 'https://github.com/elston-jja/KnotsAndCrosses https://github.com/SPOCKnots/pyknotid https://github.com/jorgeatorres/knot-that-easy https://github.com/Algebra8/Knots'
    urls = 'https://github.com/bisq-network/bisq'
    urls = 'https://github.com/bisq-network/bisq-docs https://github.com/bisq-network/wiki'
    urls = 'https://github.com/click-contrib/click-spinner'
    urls = 'https://github.com/gioui/gio https://github.com/gioui/gio-example'
    urls = 'https://github.com/TLowry/npp-golang https://github.com/golang/go github.com/urfave/cli'
    urls = 'https://github.com/vsariola/sointu/ https://github.com/marcusvolz/mathart'
    urls = 'https://github.com/itchyny/volume-go https://github.com/pipelined/vst2'
    urls = 'https://github.com/netwide-assembler/nasm'
    urls = 'https://github.com/biessek/golang-ico'
    urls = 'https://github.com/wailsapp/docsv1'
    urls = 'https://github.com/Zulko/moviepy'
    urls = 'https://github.com/sublimetext-io/docs.sublimetext.io'
    urls = 'https://github.com/ChrisTitusTech/win10script'
    urls = 'https://github.com/TLowry/npp-golang'
    urls = 'https://github.com/kendfss/SampleFinder https://github.com/beschulz/wav2png https://github.com/brackeen/ok-file-formats https://github.com/cslashm/ECPy https://github.com/strawberry-graphql/strawberry https://github.com/XanaduAI/StrawberryFields'
    urls = 'https://github.com/TheAlgorithms/Python https://github.com/numpy/numpy'
    urls = 'https://github.com/wbond/package_control https://github.com/SublimeCodeIntel/SublimeCodeIntel git clone https://github.com/ozankasikci/vim-man https://github.com/learnbyexample/vim_reference https://github.com/iggredible/Learn-Vim https://github.com/nathanaelkane/vim-indent-guides'
    urls = 'https://github.com/python/cpython'
    urls = 'https://github.com/birkenfeld/fddf https://github.com/kochampsy/fractal https://github.com/birkenfeld/serde-pickle https://github.com/gvanrossum/patma https://github.com/aosabook/500lines https://github.com/HypothesisWorks/hypothesis/tree/master/hypothesis-python https://github.com/marin-m/SongRec https://github.com/mrdoob/three.js/'
    urls = 'https://github.com/kendfss/numpy'
    urls = 'https://github.com/SublimeCodeIntel/CodeIntel https://github.com/numpy/numpy.org'
    urls = 'https://github.com/python-pillow/Pillow https://github.com/aristofun/py-agender https://github.com/MeteHanC/Python-Median-Filter https://github.com/bes-dev/random_face https://github.com/luigivieira/emotions https://github.com/hugolgst/digart'
    urls = 'https://github.com/VladimirMarkelov/clui'
    urls = 'https://github.com/golang/go.wiki.git https://github.com/maxence-charriere/go-app https://github.com/webview/webview https://github.com/boppreh/keyboard https://github.com/asweigart/pyautogui https://github.com/boppreh/mouse https://github.com/kendfss/objregex https://github.com/boppreh/replace_me https://github.com/zserge/webview-python https://github.com/zserge/1bitr https://github.com/kendfss/awfice https://github.com/zserge/glob-grep https://github.com/zserge/nokia-composer https://github.com/kendfss/beep https://github.com/zserge/chess https://github.com/kendfss/metric https://github.com/zserge/lorca'
    urls = 'https://github.com/mingrammer/pyreportcard https://github.com/bear/python-twitter/'
    urls = 'https://github.com/twitterdev/twitter-python-ads-sdk https://github.com/twitterdev/search-tweets-python'
    urls = 'https://github.com/wuub/SublimeREPL'
    urls = 'https://github.com/leanprover/elan https://github.com/leanprover/lean4 https://github.com/leanprover/lean https://github.com/leanprover/vscode-lean https://github.com/leanprover/lean.vim https://github.com/leanprover/tutorial'
    urls = 'https://github.com/ncatlab/nlab-content-html https://github.com/ncatlab/nlab https://github.com/ncatlab/nlab-core https://github.com/ImperialCollegeLondon/natural_number_game'
    urls = 'https://github.com/zserge/carnatus'
    urls = 'https://github.com/steambap/png-to-ico'
    urls = 'https://github.com/mavillan/py-hausdorff https://github.com/microsoft/winget-cli https://github.com/mozilla/geckodriver https://github.com/python/devguide'
    urls = 'https://github.com/kendfss/cpython'
    urls = 'https://github.com/ktaranov/sqlserver-kit'
    urls = 'git.sr.ht/~adnano/go-gemini '
    urls = 'https://tildegit.org/sloum/gemini-vim-syntax https://github.com/makeworld-the-better-one/gemlikes https://github.com/cbrews/ignition https://github.com/makeworld-the-better-one/md2gemini https://github.com/michael-lazar/gemini-diagnostics https://github.com/huntingb/gemtext-html-converter https://github.com/michael-lazar/jetforce https://tildegit.org/solderpunk/gemini-demo-1 https://tildegit.org/solderpunk/gemini-demo-3 https://github.com/pitr/gig https://github.com/skyjake/lagrange'
    urls = 'https://github.com/tgree/svg_plot'
    urls = 'https://github.com/lace/hobart-svg https://github.com/naveen521kk/text2svg'
    urls = 'https://github.com/TiagoBras/svg2code'
    urls = 'https://github.com/golang/sys'
    urls = 'https://github.com/fiefdx/CallingViewer https://github.com/skratchdot/open-golang'
    urls = 'https://github.com/psf/black github.com/go-playground/validator github.com/boombuler/barcode github.com/dghubble/oauth1 github.com/go-sql-driver/mysql github.com/uniplaces/carbon https://github.com/beego/beedoc https://github.com/bitwarden/desktop' 
    urls = 'https://github.com/twitterdev/search-tweets-python https://github.com/grammakov/USA-cities-and-states'
    # urls = 'https://github.com/regebro/svg.path https://github.com/kyamagu/psd2svg'
    urls = 'github.com/go-playground/validator github.com/Jeffail/gabs github.com/montanaflynn/stats github.com/wcharczuk/go-chart github.com/thoas/go-funk github.com/PuerkitoBio/goquery github.com/mingrammer/commonregex github.com/disintegration/imaging github.com/antchfx/xmlquery github.com/antchfx/xpath github.com/jinzhu/now'
    urls = 'https://github.com/pim-book/programmers-introduction-to-mathematics https://github.com/j2kun/fft https://github.com/pim-book/exercises https://github.com/j2kun/svd https://github.com/j2kun/essays https://github.com/j2kun/restrepo-1957 https://github.com/j2kun/fft-watermark https://github.com/j2kun/collatz-visualization https://github.com/j2kun/canvas-scripts https://github.com/j2kun/riemann-divisor-sum https://github.com/jeroennoels/john-baez-challenge https://github.com/a-kastic/CodeCogs https://github.com/r2src/top10fonts/ https://github.com/JulienPalard/oeis github.com/jtguibas/cinema https://github.com/sikang99/cinema https://github.com/Remcoman/gomovie https://github.com/AhmedAshourDev/gocma https://github.com/Microsoft/Win2D https://github.com/Microsoft/DirectXTK https://github.com/shreyas253/SylNet https://github.com/j2kun/subset-cover https://github.com/j2kun/subset-cover https://github.com/j2kun/house-buying-experiments https://github.com/j2kun/computing-homology https://github.com/j2kun/zero-knowledge-proofs https://github.com/j2kun/top-trading-cycles https://github.com/j2kun/the-mathematics-of-secret-sharing https://github.com/j2kun/simplex-algorithm https://github.com/j2kun/row-reduction https://github.com/j2kun/random-art https://github.com/j2kun/myday https://github.com/j2kun/restrepo-1957'
    urls = 'https://github.com/MacroPower/prometheus_video_renderer'
    urls = 'https://github.com/Microsoft/Win2D-samples'
    urls = 'https://github.com/tobanteAudio/juce-cookbook'
    urls = 'https://github.com/audiowaves/simpleSineWaveGenerator'
    urls = 'https://github.com/j2kun/finite-fields https://github.com/j2kun/elliptic-curve-diffie-hellman https://github.com/j2kun/row-reduction https://github.com/j2kun/cryptanalysis-n-grams https://github.com/j2kun/categories-as-types https://github.com/j2kun/boosting https://github.com/j2kun/1on1-questions https://github.com/j2kun/bezier-picasso'
    urls = 'https://github.com/tiangolo/typer '
    urls = 'https://github.com/kendfss/filetype.py https://github.com/kendfss/toot https://github.com/j2kun/ball-game'
    urls = 'https://github.com/juce-framework/JUCE'
    urls = 'https://github.com/praveenpenumaka/numpygo github.com/soheilhy/args'
    urls = 'https://github.com/cpmech/gosl https://github.com/gonum/gonum'
    urls = 'https://git.sr.ht/~eliasnaur/gio-example https://git.sr.ht/~eliasnaur/gio'
    urls = 'https://github.com/kendfss/pyinstaller'
    urls = 'https://github.com/vsariola/sointu/'
    # urls = 'https://github.com/netwide-assembler/nasm'
    # urls = 'github.com/Arafatk/glot https://github.com/vdobler/chart https://github.com/wcharczuk/go-chart github.com/kylelemons/go-gypsy/yaml gopkg.in/yaml.v2 github.com/davecgh/go-spew github.com/sjwhitworth/golearn'
    # urls = 'https://github.com/chrislusf/glow github.com/vugu/vugu'
    # urls = 'https://github.com/golang/go.wiki.git https://github.com/andybalholm/c2go'
    urls = 'https://github.com/thanhpk/randstr https://github.com/microsoft/terminal https://github.com/goombaio/guid'
    # urls = 'https://github.com/ChrisTitusTech/win10script'
    # urls = 'https://github.com/vugu/vugu'
    # urls = 'https://github.com/kendfss/win10script'
    # urls = 'https://github.com/kendfss/AIX-Converter https://github.com/AdamSteffanick/ipa-data https://github.com/kendfss/string_to_ipa https://github.com/mphair/pyipa https://github.com/AbiWord/enchant https://github.com/pyenchant/pyenchant https://github.com/dmort27/epitran https://github.com/pettarin/ipapy https://github.com/mCodingLLC/Anaphones https://github.com/mCodingLLC/VideosSampleCode'
    # urls = 'https://github.com/kendfss/ipa-data  https://github.com/Alexir/CMUdict'
    # urls = 'https://github.com/h2non/filetype.py https://github.com/h2non/filetype https://github.com/h2non/jshashes  github.com/h2non/bimg https://github.com/emirpasic/gods https://github.com/cdgriffith/puremagic https://github.com/schlerp/pyfsig'
    urls = 'https://github.com/postgres/postgres'
    urls = 'https://github.com/rafael-fuente/Diffraction-Simulations--Angular-Spectrum-Method'
    urls = 'https://github.com/kendfss/Diffraction-Simulations--Angular-Spectrum-Method'
    urls = 'https://github.com/simp7/nonograminGo https://github.com/trknhr/2048-go https://github.com/guillaumebreton/gone'
    urls = 'https://github.com/docschina/GFM-docs https://github.com/markdown/markdown.github.com.wiki.git https://github.com/markdown/markdown.github.com'
    urls = 'https://github.com/go-p5/p5'
    urls = 'https://git.sr.ht/~whereswaldon/gio-x'
    urls = 'https://github.com/HFO4/gameboy.live https://github.com/adg/game https://github.com/hajimehoshi/ebiten https://github.com/faiface/pixel https://github.com/faiface/pixel-examples https://github.com/danicat/pacgo https://github.com/DyegoCosta/snake-game https://github.com/hajimehoshi/oto https://github.com/Humpheh/goboy https://github.com/u2i/superstellar https://github.com/xwjdsh/2048-ai https://github.com/danaugrs/gokoban https://github.com/g3n/g3nd https://github.com/hcrgm/Gobang-Go https://github.com/jak103/uno https://github.com/Lallassu/gizmo https://github.com/gophergala/golab https://github.com/yulrizka/fam100 https://github.com/a8m/play https://github.com/KyleBanks/conways-gol https://github.com/yinwhm12/leaf_game'
    urls = 'https://github.com/adammck/sixaxis'
    urls = 'https://github.com/kendfss/snake-game https://github.com/kendfss/2048-go'
    urls = 'https://github.com/colormine/colormine https://github.com/muak/ColorMinePortable'
    # urls = 'https://tildegit.org/fluora/modu https://tildegit.org/fluora/irradiate https://tildegit.org/fluora/hecc https://tildegit.org/sloum/filtress'
    urls = 'https://github.com/nikhilkumarsingh/prettype https://github.com/nikhilkumarsingh/content-downloader https://github.com/miguelgrinberg/flask-video-streaming https://github.com/kendfss/Best-README-Template'
    urls = 'https://github.com/katzien/go-structure-examples'
    urls = 'https://github.com/xujiajun/nutsdb https://github.com/matt4biz/go-class-racer https://github.com/matt4biz/go-class-counts https://github.com/mjibson/go-dsp https://github.com/eugene-eeo/orchid https://github.com/kendfss/orchid https://github.com/hajimehoshi/oto https://github.com/kendfss/waveform https://github.com/kendfss/mix https://github.com/mewkiz/flac https://github.com/kendfss/htm https://github.com/kendfss/cell https://github.com/go-gl/glfw https://github.com/kendfss/vizi https://github.com/dskinner/snd https://github.com/AuLib/AuLib https://github.com/faiface/beep https://github.com/faiface/beep.wiki.git https://github.com/aubio/aubio'
    urls = 'https://github.com/kendfss/evalfilter '
    urls = 'https://github.com/kendfss/dirty-limericks https://github.com/kendfss/vst2 https://github.com/kendfss/NNfSiX'
    urls = 'https://github.com/pipelined/fileformat https://github.com/pipelined/signal https://github.com/pipelined/pipe https://github.com/pipelined/portaudio'
    urls = 'https://github.com/pipelined/example'
    urls = 'https://github.com/gordonklaus/portaudio'
    urls = 'https://github.com/kendfss/cpython https://github.com/tensorflow/tensorflow https://github.com/minimaxir/textgenrnn'
    urls = 'https://github.com/wingtk/gvsbuild'
    urls = 'https://gitlab.gnome.org/GNOME/gtk'
    urls = 'https://github.com/urfave/cli'
    urls = 'https://github.com/GeertJohan/gomatrix https://github.com/rgm3/gomandelbrot https://github.com/wtfutil/wtf https://github.com/tmountain/uchess https://github.com/atotto/clipboard'
    urls = 'https://github.com/HackerPoet/FractalSoundExplorer https://github.com/HackerPoet/Chaos-Equations https://github.com/HackerPoet/NonEuclidean https://github.com/nigels-com/glew https://github.com/HackerPoet/Trackpad'
    urls = 'https://github.com/jasonwebb/morphogenesis-resources https://github.com/fogleman/dlaf https://github.com/inconvergent/differential-line https://github.com/jasonwebb/2d-space-colonization-experiments'
    urls = 'git://github.com/ninja-build/ninja.git https://github.com/kardianos/pdf https://github.com/cockroachdb/apd https://github.com/kardianos/osext'
    urls = 'https://github.com/gtk-rs/gtk3-rs'
    urls = 'https://github.com/ayoisaiah/f2'
    urls = 'https://github.com/kendfss/f2'
    urls = 'https://github.com/kendfss/youtube-dl'
    urls = 'https://github.com/kendfss/Leiserchess---MIT-6.172-Fall16-Final-Project'
    urls = 'https://github.com/jadefox10200/goprint'
    urls = 'https://github.com/tmountain/uchess'
    urls = 'https://github.com/nsf/termbox-go'
    urls = 'https://github.com/PDFTron/PDFNetWrappers'
    urls = 'https://github.com/tmountain/take4 https://github.com/evancz/guide.elm-lang.org https://github.com/evancz/elm-todomvc https://github.com/tmountain/note-teacher'
    urls = 'github.com/mattn/go-runewidth https://github.com/nwtgck/gif-progress'
    urls = 'https://github.com/boisgera/bitstream'
    urls = 'https://github.com/Zulko/moviepy'
    urls = 'github.com/TheZoraiz/ascii-image-converter'
    urls = 'https://github.com/Zulko/gizeh'
    urls = 'https://github.com/xfrr/goffmpeg'
    urls = 'https://github.com/floostack/transcoder github.com/stretchr/testify'
    urls = 'github.com/stretchr/objx'
    urls = 'https://github.com/mrdoob/texgen.js https://github.com/kendfss/musicblocks '
    urls = 'https://github.com/kendfss/vst2'
    urls = 'https://github.com/cstanze/anarchy-angola'
    urls = 'https://github.com/kendfss/python-barcode https://github.com/kendfss/Pillow https://github.com/Kozea/CairoSVG/'
    urls = 'https://github.com/GNOME/librsvg'
    urls = 'https://github.com/Venti-/pubcode'
    urls = 'https://github.com/kendfss/uchess'
    urls = 'https://gitlab.com/gomidi/midi/ https://github.com/brettbuddin/shaden https://github.com/brettbuddin/reverb https://github.com/brettbuddin/fourier'
    urls = 'https://github.com/brettbuddin/musictheory'
    urls = 'https://github.com/tholman/generative-artistry/ https://github.com/kendfss/shaden https://github.com/pippinbarr/chesses https://github.com/pippinbarr/itisasifyouweredoingwork'
    urls = 'https://github.com/boisgera/bitstream'
    urls = 'https://github.com/KyleBanks/conways-gol https://github.com/go-gl/example https://github.com/go-gl/mathgl https://github.com/go-gl/gltext https://github.com/go-gl/osmesa https://github.com/go-gl/gldebug'
    urls = 'github.com/go-gl/glfw'
    urls = 'https://github.com/KyleBanks/conways-gol'
    urls = 'https://github.com/go-gl/gl'
    urls = 'https://github.com/glfw/glfw'
    urls = 'https://github.com/go-gl/glow'
    urls = 'https://github.com/golang-design/clipboard https://github.com/atotto/clipboard'
    urls = 'https://github.com/maurock/snake-ga https://github.com/maurock/snake-ga-tf'
    urls = 'https://github.com/masa16/narray https://github.com/gbuesing/kmeans-clusterer https://github.com/daugaard/q-learning-simple-game'
    urls = 'https://github.com/processing/processing-doclet https://github.com/processing/processing-docs'
    urls = 'https://github.com/KdotJPG/OpenSimplex2'
    urls = 'https://github.com/Megaprog/Iterators'
    urls = 'https://github.com/timrodenbroeker/tutorials'
    urls = 'https://github.com/googlefonts/spacemono https://github.com/googlefonts/roboto https://github.com/timrodenbroeker/THE-BACH-PROJECT https://github.com/googlefonts/dm-mono https://github.com/googlefonts/RobotoMono'
    urls = 'https://github.com/kendfss/english-words'
    urls = 'https://github.com/msgul/go-bitcoin-block-parser'
    urls = 'https://github.com/pterm/pterm https://github.com/mycroft/generate-genesis https://github.com/kendfss/bitcoin-rpc-client https://github.com/bibajz/bitcoin-python-async-rpc'
    urls = 'https://gitlab.com/Nevax/FreedomOS'
    urls = 'https://github.com/teh-cmc/go-internals https://github.com/go-echarts/go-echarts'
    urls = 'https://github.com/iovisor/bcc'
    urls = 'https://github.com/jiffyclub/snakeviz/'
    urls = 'https://github.com/encode/httpx'
    urls = 'https://github.com/manifoldco/promptui'
    urls = 'https://github.com/code-bullet/WorldsHardestGameAI'
    urls = 'https://github.com/nilsberglund-orleans/YouTube-simulations'
    urls = 'https://github.com/ciprian-chelba/1-billion-word-language-modeling-benchmark'
    urls = 'https://github.com/srinidhinandakumar/hidden-markov-models https://github.com/srinithish/Aritificial-Intelligence-Part-of-speech-tagging https://github.com/tvasil/pos-tagger https://github.com/agonopol/go-stem https://github.com/onlyuser/parse-english github.com/algorithmiaio/algorithmia-go https://github.com/gutfeeling/word_forms'
    urls = 'https://gitlab.com/microo8/photon'
    urls = 'https://git.sr.ht/~ghost08/photon'
    urls = 'https://github.com/processing/processing.wiki.git'
    urls = 'https://github.com/protocolbuffers/protobuf-go'
    urls = 'https://gitlab.com/KevinRoebert/ClearUrls'
    urls = 'https://github.com/mozilla/webextension-polyfill https://github.com/web-ext-labs/create-web-ext https://github.com/web-ext-labs/ui-tool'
    urls = 'https://github.com/llvm/llvm-project.git'
    urls = 'https://github.com/ertdfgcvb/Scam'
    urls = 'https://github.com/algorandfoundation/specs https://github.com/algorandfoundation/ARCs https://github.com/HashMapsData2Value/AlgorandFAQ https://github.com/Sonlis/AlgoDecentralizedMarket https://github.com/emg110/algorand-qrcode https://github.com/RootSoft/flutter-algorand-wallet https://github.com/gidonkatten/flipping-a-coin https://github.com/dashboardblock/themonopolybank.git https://github.com/algorandfoundation/buildweb3 github.com/algorand/go-algorand-sdk https://github.com/algorand/indexer https://github.com/algorand/docs https://github.com/algorand/sandbox https://github.com/algorand/mule https://github.com/algorand/workpool https://github.com/algorand/xorfilter https://github.com/algorand/workpool https://github.com/ipaleka/algodjango https://github.com/algorand/py-algorand-sdk'
    urls = 'https://github.com/bitwarden/browser https://github.com/prateek3255/replacely https://github.com/codelucas/newspaper https://github.com/cnwangjie/better-onetab'
    urls = 'https://github.com/gohugoio/hugo.git'
    urls = 'https://github.com/gohugoio/hugoDocs'
    urls = 'https://github.com/raditzlawliet/go-grpc-example'
    urls = 'https://github.com/asciinema/asciinema.git https://github.com/chjj/ttystudio https://github.com/termbacktime/termbacktime'
    urls = 'https://github.com/sorenisanerd/gotty https://github.com/charmbracelet/harmonica'
    urls = 'https://github.com/Gyro7/mangodl'
    urls = 'https://github.com/go-tk/di https://github.com/aquasecurity/libbpfgo https://github.com/mehrdadrad/radvpn https://github.com/net-byte/vtun'
    urls = 'https://github.com/unsafecast/soundplot https://github.com/liamg/gifwrap https://github.com/kendfss/gca https://github.com/soypat/gitaligned'
    urls = 'https://github.com/quackduck/secret https://github.com/mattn/go-generics-example https://github.com/kendfss/readme https://github.com/eleby/pixelizer https://github.com/dolthub/dolt/ https://github.com/jdxyw/generativeart https://github.com/SignTools/ios-signer-service https://github.com/xen0bit/botnet-fishbowl'
    urls = 'https://github.com/Narasimha1997/fake-sms https://github.com/anuraghazra/github-readme-stats https://github.com/soypat/rebed https://github.com/cblgh/lieu https://github.com/lizrice/libbpfgo-beginners https://github.com/lizrice/ebpf-beginners https://github.com/lizrice/containers-from-scratch https://github.com/lizrice/strace-from-scratch https://github.com/hmailserver/hmailserver/ https://github.com/irevenko/what-anime-cli https://github.com/bahlo/go-styleguide https://github.com/zhoreeq/ipfd https://github.com/hoorayman/unitalk'
    urls = 'https://github.com/nsqio/nsq https://github.com/nsqio/go-nsq https://github.com/nsqio/nsqio.github.io'
    urls = 'https://github.com/VividCortex/go-database-sql-tutorial'
    urls = 'https://github.com/kendfss/kendfss https://github.com/WillHayCode/unicode-flag-finder/'
    urls = 'https://github.com/dolthub/docs'
    urls = 'https://github.com/enescakir/emoji'
    urls = 'github.com/go-sql-driver/mysql'
    urls = 'https://github.com/kendfss/mangodl'
    urls = 'https://github.com/gohugoio/hugoDocs github.com/gohugoio/hugo.git'
    urls = 'https://github.com/jayco/go-emoji-flag'
    urls = 'https://github.com/cvzi/flag'
    urls = 'https://github.com/postmanlabs/postman-docs'
    urls = 'golang.org/x/mobile/example/audio golang.org/x/mobile/example/basic'
    urls = 'golang.org/x/mobile/example'
    urls = 'https://github.com/SignTools/ios-signer-service https://github.com/SignTools/ios-signer-service https://github.com/SignTools/ios-signer-ci https://github.com/SignTools/altserver-cert-dumper'
    urls = 'https://github.com/ViRb3/PerfectProxyDLL'
    urls = 'github.com/cespare/reflex'
    urls = 'https://github.com/radovskyb/watcher'
    urls = 'https://github.com/kendfss/watcher'
    urls = 'https://github.com/meshhq/golang-html-template-tutorial'
    urls = 'https://github.com/Programming-Duck/carousel'
    urls = 'https://github.com/gorilla/mux https://github.com/gorilla/websocket https://github.com/gorilla/sessions https://github.com/gorilla/handlers https://github.com/gorilla/schema https://github.com/gorilla/csrf'
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    # urls = ''
    
    
    main(urls)
