import React from "react";

const Treshold = ({
  isToggled,
  tempHome,
  heatingTemp,
  classStyle1,
  classStyle2,
  text,
}) => {
  return (
    <div>
      <div
        className={
          isToggled === true && tempHome < heatingTemp
            ? classStyle1 
            : classStyle2
        }
      >
        {heatingTemp} <sup className="text-lg">{text}</sup>
      </div>
    </div>
  );
};

export default Treshold;
