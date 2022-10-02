import type { NextPage } from "next";
import { useEffect, useState } from "react";

const Home: NextPage = () => {
  const [valueAddress, setValueAddress] = useState("");
  const [valueSubject, setValueSubject] = useState("");
  const [valueBody, setValueBody] = useState("");
  const [valueAudio, setValueAudio] = useState();
  const [valueAudioName, setValueAudioName] = useState("test.mp3");

  const handleInputAddress = (e: any) => {
    setValueAddress(e.target.value);
  };

  const handleInputSubject = (e: any) => {
    setValueSubject(e.target.value);
  };

  const handleInputBody = (e: any) => {
    setValueBody(e.target.value);
  };

  const handleInputAudio = (e: any) => {
    let file = e.target.files[0];
    // console.log(file);
    setValueAudioName(file?.name)
    let reader = new FileReader();
    reader.onloadend = function () { //@ts-ignore
      setValueAudio(reader.result)
    };
    if(file) reader.readAsDataURL(file);
    // setValueAudio(e.target.value);
  };

  useEffect(() => {
    //@ts-ignore
    // console.log(valueAddress, valueSubject, valueBody, valueAudio, valueAudioName);
  }, [valueAddress, valueSubject, valueBody, valueAudio]);

  return (
    <div className="flex items-center justify-center mt-[20%]">
      <div className="text-4xl flex flex-col w-max p-4 border-2 border-black rounded-lg">
        <p className="text-center">send mail</p>
        <div className="flex items-center mt-2">
          <p>address</p>
          <input
            value={valueAddress}
            type="text"
            className={`ml-2`}
            onChange={handleInputAddress}
          />
        </div>
        <div className="flex items-center mt-2">
          <p>subject</p>
          <input
            value={valueSubject}
            type="text"
            className={`ml-2`}
            onChange={handleInputSubject}
          />
        </div>
        <div className="flex items-center mt-2">
          <p>body</p>
          <input
            value={valueBody}
            type="text"
            className={`ml-2`}
            onChange={handleInputBody}
          />
        </div>
        <div className="flex items-center mt-2">
          <p>audio</p>
          {/* @ts-ignore */}
          <input
            id="Audiofile"
            onChange={(e) => handleInputAudio(e)}
            type="file"
            accept=".mp3"
          />
        </div>
        <button className='mt-1 border rounded-md border-black w-max '>Жми, екарный бабай</button>
      </div>
    </div>
  );
};

export default Home;
