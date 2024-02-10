import Header from './components/Header';
import SendAV from './components/Upload';

const AddReport = () => {
    return (
        <div className="flex flex-col w-full h-screen overflow-y-hidden items-center">
            <Header/>
            <SendAV/>
        </div>
    );
}

export default AddReport;